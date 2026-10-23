#!/usr/bin/env python3
"""
Conferidor externo dos arquivos vivos de um Project-filho, rodado no ateliê
depois da sessão (skill conferencia-de-sessao). Confere caderno, CSV de
cartões, notas de melhoria e prompt de estado contra o TEMPLATE do caderno,
o CONTRATO do CSV da analise-desempenho e o BACKLOG do ateliê, e classifica
cada achado num dos três baldes:

    pequeno  mecânico, sem juízo, reversível -> proposta de edição pronta
    medio    depende de diagnóstico ou do que foi dito na sessão -> perguntar
    grande   estrutural, regra de skill não cumprida -> backlog

Uso:
    python conferir_sessao.py <pasta-da-disciplina> \
        --template atelie/caderno-DISCIPLINA-template.md \
        --backlog  atelie/backlog-atelie.md \
        [--analise <SKILL.md da analise-desempenho>] \
        [--json relatorio.json] [--propor-edicoes DIR --data AAAA-MM-DD]

Sem eco (D16): o script não guarda cabeçalho de tabela, vocabulário nem
contrato do CSV. Lê os três da fonte a cada execução: o template (linhas-modelo
T1/E1/F1 e células "a / b / c"), a seção "Contrato do arquivo" da
analise-desempenho e o inventário e as fricções do backlog. O que fica aqui
é só o NOME do que se confere (VOCAB_COLUNAS e os rótulos de seção), como
ponteiro. Se a fonte mudar, a checagem muda junto; se a fonte sumir, a
checagem é pulada e o relatório diz qual e por quê, sem cair num valor velho.

O script SINALIZA e PROPÕE. Não grava em arquivo vivo nenhum: as edições
propostas saem como edicoes-<arquivo>.json para o aplicar_edicoes.py
(entrega-de-artefato, modo --carimbo), depois do "sim" do aluno.
"""

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

# Ponteiros nomeados (D16): QUAIS colunas têm vocabulário controlado. Os
# VALORES vêm da linha-modelo do template, nunca daqui.
VOCAB_COLUNAS = ["Veredito", "Eixo", "Carga", "Tipo", "Status", "Afeta o gabarito?"]
# Colunas cujo valor pode juntar dois termos do vocabulário (entrada mista).
VOCAB_MULTIPLO = {"Eixo"}

PENDENCIA = re.compile(r"a transcrever|a confirmar", re.I)
DATA = re.compile(r"\d{4}-\d{2}-\d{2}")

BALDES = ("pequeno", "medio", "grande")


# ---------------------------------------------------------------- utilidades

def ler(p):
    return Path(p).read_text(encoding="utf-8")


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def limpo(s):
    """Tira marcação markdown (negrito, itálico, código) e espaços."""
    return re.sub(r"[*_`]", "", s).strip()


def norm_cab(s):
    return re.sub(r"\s+", " ", limpo(s)).strip().lower()


def celulas(linha):
    partes = re.split(r"(?<!\\)\|", linha.rstrip("\n"))
    return [c.strip() for c in partes[1:-1]]


def eh_separador(cel):
    return all(re.fullmatch(r":?-{3,}:?", c.strip()) for c in cel if c.strip()) and any(cel)


def ids(texto, letra):
    return [int(n) for n in re.findall(rf"\b{letra}(\d+)\b", texto)]


def casa(v, opcao):
    """Valor contra uma opção do template; '[data]' na opção vira data opcional."""
    o = opcao.lower().strip()
    if "[" in o:
        base = o.split("[")[0].strip()
        return v == base.split()[0] or v.startswith(base)
    return v == o


def parse_data(s, base=None):
    """'2026-10-13 a 17', '2026-09-29/30', '2026-09-17 a 2026-09-22' -> (ini, fim)."""
    s = limpo(s)
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    if not m:
        return None
    ini = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    resto = s[m.end():]
    m2 = re.match(r"\s*(?:a|/|–|-)\s*(\d{4}-\d{2}-\d{2}|\d{1,2})\b", resto)
    fim = ini
    if m2:
        v = m2.group(1)
        if DATA.fullmatch(v):
            y, mo, d = map(int, v.split("-"))
            fim = date(y, mo, d)
        else:
            try:
                fim = date(ini.year, ini.month, int(v))
            except ValueError:
                fim = ini
    return ini, fim


# ------------------------------------------------------------ modelo do doc

class Doc:
    """Documento markdown fatiado por cabeçalho; guarda as tabelas de cada seção."""

    def __init__(self, texto):
        self.texto = texto
        self.linhas = texto.split("\n")
        self.secoes = []   # (chave, titulo, nivel, n_linha)
        self.tabelas = {}  # chave -> lista de tabelas; tabela = dict
        chave = "_topo"
        bloco = []
        inicio = None
        for i, l in enumerate(self.linhas):
            m = re.match(r"^(#{2,4})\s+(.*)$", l)
            if m:
                self._fecha(chave, bloco, inicio)
                bloco, inicio = [], None
                chave = self._chave(m.group(2), len(m.group(1)))
                self.secoes.append((chave, m.group(2).strip(), len(m.group(1)), i))
                continue
            if l.startswith("|"):
                if not bloco:
                    inicio = i
                bloco.append(l)
            elif bloco:
                self._fecha(chave, bloco, inicio)
                bloco, inicio = [], None
        self._fecha(chave, bloco, inicio)

    @staticmethod
    def _chave(titulo, nivel):
        m = re.match(r"(\d+\.\d+)\b", titulo)
        if m:
            return m.group(1)
        m = re.match(r"Se[cç][aã]o\s+(\d+)", titulo, re.I)
        if m:
            return f"S{m.group(1)}"
        return "~" + norm_cab(titulo)

    def _fecha(self, chave, bloco, inicio):
        if not bloco:
            return
        cab = celulas(bloco[0])
        tem_sep = len(bloco) > 1 and eh_separador(celulas(bloco[1]))
        dados = []
        for k, l in enumerate(bloco[2 if tem_sep else 1:], start=(2 if tem_sep else 1)):
            dados.append((inicio + k, l, celulas(l)))
        self.tabelas.setdefault(chave, []).append(
            {"cab": cab, "sep": tem_sep, "dados": dados, "linha": inicio})

    def tabela(self, chave):
        t = self.tabelas.get(chave)
        return t[0] if t else None

    def linha_que_comeca(self, prefixo):
        for i, l in enumerate(self.linhas):
            if l.startswith(prefixo):
                return i, l
        return None, None


def col(tab, nome):
    alvo = norm_cab(nome)
    for k, c in enumerate(tab["cab"]):
        if norm_cab(c) == alvo:
            return k
    return None


def valor(tab, linha_cel, nome):
    k = col(tab, nome)
    if k is None or k >= len(linha_cel):
        return None
    return linha_cel[k]


def linhas_reais(tab, modelo=None):
    """Linhas de dados que não são vazias nem cópia da linha-modelo do template."""
    out = []
    for n, l, c in tab["dados"]:
        if not any(limpo(x) for x in c):
            continue
        if modelo is not None and [limpo(x) for x in c] == [limpo(x) for x in modelo]:
            continue
        out.append((n, l, c))
    return out


# ------------------------------------------------------- leitura das fontes

def ler_template(caminho):
    """Do template: seções, cabeçalhos, linha-modelo, vocabulário e rótulos do carimbo."""
    doc = Doc(ler(caminho))
    secoes = {ch: t for ch, t, nv, _ in doc.secoes if not ch.startswith("~")}
    tabelas, vocab = {}, {}
    for ch, tabs in doc.tabelas.items():
        if ch.startswith("~") or ch == "_topo":
            continue
        t = tabs[0]
        modelo = t["dados"][0][2] if t["dados"] else []
        tabelas[ch] = {"cab": t["cab"], "modelo": modelo}
        for nome in VOCAB_COLUNAS:
            k = col(t, nome)
            if k is not None and k < len(modelo) and "/" in modelo[k]:
                opcoes = [o.strip() for o in limpo(modelo[k]).split(" / ")]
                vocab[(ch, nome)] = opcoes
    _, carimbo = doc.linha_que_comeca("> **Última atualização:**")
    rotulos = re.findall(r"\*\*([^*]+?):\*\*", carimbo or "")
    return {"secoes": secoes, "tabelas": tabelas, "vocab": vocab, "rotulos": rotulos}


def ler_contrato(caminho):
    """Linhas '#chave:valor' do bloco de código da seção 'Contrato do arquivo'."""
    if not caminho:
        return None
    texto = ler(caminho)
    m = re.search(r"#+\s*Contrato do arquivo(.*?)```\s*\n(.*?)```", texto, re.S)
    if not m:
        return None
    contrato = {}
    for l in m.group(2).split("\n"):
        mm = re.match(r"#([^:]+):(.*)$", l.strip())
        if mm:
            contrato[mm.group(1).strip()] = mm.group(2)
    return contrato


def achar_analise():
    """Procura o SKILL.md da analise-desempenho nos lugares onde as skills
    ficam montadas (chat web: /mnt/skills; Claude Code: ~/.claude/skills).
    Pasta sem permissão é pulada; se nada for achado, a checagem 8 é pulada
    e o relatório diz isso — nunca um contrato de reserva."""
    raizes = ["/mnt/skills", str(Path.home() / ".claude/skills"), "/root/.claude/skills"]
    for raiz in raizes:
        try:
            p = Path(raiz)
            if not p.is_dir():
                continue
            for s in p.rglob("SKILL.md"):
                if s.parent.name == "analise-desempenho":
                    return str(s)
        except (PermissionError, OSError):
            continue
    return None


# ----------------------------------------------------------------- relatório

class Relatorio:
    def __init__(self):
        self.achados = []
        self.puladas = []
        self.notas = []

    def add(self, balde, chk, arquivo, msg, linha=None, edicao=None, grupo=None):
        assert balde in BALDES
        self.achados.append({"balde": balde, "checagem": chk, "arquivo": arquivo,
                             "linha": (linha + 1) if linha is not None else None,
                             "msg": msg, "edicao": edicao, "grupo": grupo})

    def pular(self, chk, motivo):
        self.puladas.append({"checagem": chk, "motivo": motivo})


# ----------------------------------------------------------------- caderno

def conferir_caderno(path, tpl, rel, n_cartoes, hoje):
    nome = Path(path).name
    doc = Doc(ler(path))
    estrutura_grande = False
    carimbo_fix = {}  # rotulo -> novo texto do segmento

    # --- 3. estrutura x template ------------------------------------------
    for ch, titulo in tpl["secoes"].items():
        achou = [s for s in doc.secoes if s[0] == ch]
        if not achou:
            rel.add("grande", 3, nome, f"seção do template ausente: '{titulo}'", grupo="estrutura")
            estrutura_grande = True
        elif norm_cab(achou[0][1]) != norm_cab(titulo):
            n = achou[0][3]
            nivel = "#" * achou[0][2]
            rel.add("pequeno", 3, nome, f"título de seção diverge do template: '{achou[0][1]}' → '{titulo}'",
                    linha=n, grupo="estrutura",
                    edicao={"ancora": doc.linhas[n], "texto": f"{nivel} {titulo}"})
    for ch, t in tpl["tabelas"].items():
        tab = doc.tabela(ch)
        if tab is None:
            if ch in tpl["secoes"] and any(s[0] == ch for s in doc.secoes):
                rel.add("grande", 3, nome, f"seção {ch} sem a tabela do template", grupo="estrutura")
                estrutura_grande = True
            continue
        esperado = [norm_cab(c) for c in t["cab"]]
        real = [norm_cab(c) for c in tab["cab"]]
        it = iter(real)
        em_ordem = all(c in it for c in esperado)
        faltam = [c for c, ce in zip(t["cab"], esperado) if ce not in real]
        if faltam or not em_ordem:
            msg = (f"tabela {ch} fora do template 2.x: faltam {faltam}" if faltam
                   else f"tabela {ch} com as colunas do template fora de ordem")
            rel.add("grande", 3, nome, msg + " (fricção 39: migrar instanciando o template)",
                    linha=tab["linha"], grupo="estrutura")
            estrutura_grande = True
        extras = [c for c in tab["cab"] if norm_cab(c) not in esperado]
        if extras and not faltam:
            rel.notas.append(f"{nome} {ch}: coluna(s) local(is) {extras} — precedente aceito (backlog 1.38)")
        if not tab["sep"]:
            rel.add("pequeno", 3, nome, f"tabela {ch} sem linha separadora", linha=tab["linha"], grupo="estrutura")
        for n, l, c in tab["dados"]:
            if len(c) != len(tab["cab"]):
                rel.add("medio", 3, nome, f"linha com {len(c)} colunas numa tabela de {len(tab['cab'])}: {limpo(l)[:70]}…",
                        linha=n)
        if len(doc.tabelas.get(ch, [])) > 1:
            rel.add("pequeno", 3, nome, f"tabela {ch} partida em {len(doc.tabelas[ch])} blocos (linha em branco dentro da tabela?)",
                    linha=doc.tabelas[ch][1]["linha"], grupo="estrutura")

    # --- carimbo -------------------------------------------------------------
    nc, carimbo = doc.linha_que_comeca("> **Última atualização:**")
    seg = {}
    if carimbo is None:
        rel.add("grande", 1, nome, "caderno sem carimbo '> **Última atualização:**' na primeira linha de citação", grupo="estrutura")
        estrutura_grande = True
    else:
        for m in re.finditer(r"\*\*([^*]+?):\*\*\s*([^·]*)", carimbo):
            seg[m.group(1).strip()] = m.group(2).strip()
        for r in tpl["rotulos"]:
            if r not in seg:
                rel.add("grande" if estrutura_grande else "pequeno", 1, nome,
                        f"carimbo sem o campo '{r}' do template", linha=nc, grupo="estrutura")

    def tab_dados(ch):
        t = doc.tabela(ch)
        modelo = tpl["tabelas"].get(ch, {}).get("modelo")
        return (t, linhas_reais(t, modelo)) if t else (None, [])

    t11, d11 = tab_dados("1.1")
    t12, d12 = tab_dados("1.2")
    t13, d13 = tab_dados("1.3")
    t14, d14 = tab_dados("1.4")
    t21, d21 = tab_dados("2.1")
    t22, d22 = tab_dados("2.2")
    tf = None
    for ch in tpl["tabelas"]:
        if tpl["tabelas"][ch]["cab"] and norm_cab(tpl["tabelas"][ch]["cab"][0]) == "#" and ch.startswith("S"):
            tf = ch
    tF, dF = tab_dados(tf) if tf else (None, [])
    if tF is None:  # Seção 3 sem número: procure tabela com F# na primeira coluna
        for ch, tabs in doc.tabelas.items():
            if any(re.fullmatch(r"F\d+", limpo(c[0])) for _, _, c in tabs[0]["dados"] if c):
                tF, dF = tabs[0], linhas_reais(tabs[0])

    texto_13 = " ".join(" ".join(c) for _, _, c in d13)

    # --- 1 e 2. numeração e carimbo T/E/F ------------------------------------
    def conferir_serie(letra, dados, rotulo, extra_declarados=""):
        nums = [int(m.group(1)) for _, _, c in dados if c and (m := re.fullmatch(rf"{letra}(\d+)", limpo(c[0])))]
        declarados_fora = set(ids(extra_declarados, letra))
        maximo = max(nums + list(declarados_fora) + [0])
        faltam = [k for k in range(1, maximo + 1) if k not in nums]
        nao_decl = [k for k in faltam if k not in declarados_fora]
        if nao_decl:
            rel.add("medio", 2, nome, f"{letra}{', '.join(letra + str(k) for k in nao_decl)} ausente(s) da tabela sem consolidação declarada — entrada sumida ou poda não registrada?")
        dup = sorted({k for k in nums if nums.count(k) > 1})
        if dup:
            rel.add("medio", 2, nome, f"{letra}# repetido: {', '.join(letra + str(k) for k in dup)}")
        if rotulo in seg:
            m = re.match(rf"{letra}(\d+)", seg[rotulo])
            if not m:
                rel.add("pequeno", 1, nome, f"carimbo '{rotulo}' sem {letra}#: '{seg[rotulo]}'", linha=nc)
            elif int(m.group(1)) != maximo:
                rel.add("pequeno", 1, nome, f"carimbo diz {rotulo} {letra}{m.group(1)}, o caderno vai até {letra}{maximo}", linha=nc)
                carimbo_fix[rotulo] = re.sub(rf"^{letra}\d+", f"{letra}{maximo}", seg[rotulo])
        return nums

    conferir_serie("T", d11, "Travamentos", texto_13 + " " + seg.get("Travamentos", ""))
    nums_e = conferir_serie("E", d12, "Erros")
    nums_f = conferir_serie("F", dF, "Erratas")

    # dossiê: 2.1 + 2.2
    if "Linhas no dossiê" in seg:
        v = seg["Linhas no dossiê"]
        n21, n22 = len(d21), len(d22)
        m = re.match(r"(\d+)(?:\s*\(2\.1\))?(?:\s*\+\s*(\d+)\s+regras?)?", v)
        ok = False
        if m:
            a = int(m.group(1))
            b = int(m.group(2)) if m.group(2) else None
            ok = (b is None and a == n21 + n22 and n22 == 0) or (b is not None and a == n21 and b == n22) \
                or (b is None and n22 == 0 and a == n21)
        if not ok:
            novo = f"{n21} (2.1)" + (f" + {n22} {'regra consolidada' if n22 == 1 else 'regras consolidadas'} (2.2)" if n22 else "")
            rel.add("pequeno", 1, nome, f"carimbo diz dossiê '{v}', as tabelas têm {n21} linha(s) na 2.1 e {n22} regra(s) na 2.2", linha=nc)
            carimbo_fix["Linhas no dossiê"] = novo

    # cartões
    if "Cartões" in seg and n_cartoes is not None:
        m = re.match(r"C?(\d+)", seg["Cartões"])
        if not m or int(m.group(1)) != n_cartoes:
            rel.add("pequeno", 1, nome, f"carimbo diz {seg['Cartões'].split('(')[0].strip()} cartões, o CSV tem {n_cartoes}", linha=nc)
            carimbo_fix["Cartões"] = re.sub(r"^C?\d+", str(n_cartoes), seg["Cartões"])

    # sessões por tipo. Uma linha do 1.4 pode ser continuação da mesma sessão
    # ("cont.", "bloco 2") ou um ciclo de várias sessões ("2026-09-17 a
    # 2026-09-22"): o número de sessões não se deduz da tabela, só se limita.
    # Mínimo = datas distintas de início; máximo = soma dos dias de cada linha.
    voc_tipo = tpl["vocab"].get(("1.4", "Tipo"))
    if t14 is not None and col(t14, "Tipo") is not None and voc_tipo and "Sessões" in seg:
        inicios = {t: set() for t in voc_tipo}
        dias = {t: 0 for t in voc_tipo}
        for _, _, c in d14:
            v = valor(t14, c, "Tipo")
            pd = parse_data(valor(t14, c, "Data") or "")
            base = re.split(r"[\s(]", limpo(v or "").lower(), maxsplit=1)[0]
            if base in inicios and pd:
                if pd[0] not in inicios[base]:
                    dias[base] += (pd[1] - pd[0]).days + 1
                inicios[base].add(pd[0])
        decl = {t: int(n) for n, t in re.findall(r"(\d+)\s+(\w+)", seg["Sessões"])}
        fora = [t for t in voc_tipo if not (len(inicios[t]) <= decl.get(t, -1) <= dias[t])]
        if fora:
            exato = all(len(inicios[t]) == dias[t] for t in voc_tipo)
            faixa = " / ".join(f"{len(inicios[t])}" + (f"–{dias[t]}" if dias[t] != len(inicios[t]) else "") + f" {t}" for t in voc_tipo)
            msg = f"carimbo diz sessões '{seg['Sessões']}', o 1.4 comporta '{faixa}'"
            if exato:
                rel.add("pequeno", 1, nome, msg, linha=nc)
                carimbo_fix["Sessões"] = " / ".join(f"{len(inicios[t])} {t}" for t in voc_tipo)
            else:
                rel.add("medio", 1, nome, msg + " — quantas sessões a linha de vários dias cobre é o aluno quem sabe", linha=nc)

    # data do carimbo x última entrada
    datas = []
    for t, dd in ((t11, d11), (t12, d12)):
        if t is None or col(t, "Data") is None:
            continue
        for _, _, c in dd:
            pd = parse_data(valor(t, c, "Data") or "")
            if pd:
                datas.append(pd[1])
    if "Última atualização" in seg and datas:
        m = DATA.match(seg["Última atualização"])
        if m:
            y, mo, d = map(int, m.group(0).split("-"))
            if date(y, mo, d) < max(datas):
                rel.add("pequeno", 1, nome, f"carimbo datado de {m.group(0)}, anterior à última entrada ({max(datas)})", linha=nc)

    # --- 4. vocabulário controlado + pendência do filho --------------------
    for (ch, nomecol), opcoes in tpl["vocab"].items():
        t = doc.tabela(ch)
        if t is None or col(t, nomecol) is None:
            continue
        falhas, total = [], 0
        for n, l, c in linhas_reais(t, tpl["tabelas"][ch]["modelo"]):
            v = valor(t, c, nomecol)
            if v is None:
                continue
            ident = limpo(c[0])[:12]
            if PENDENCIA.search(v):
                rel.add("medio", 4, nome, f"{ch} {ident}: célula '{nomecol}' pendente ('{limpo(v)[:60]}') — devolver ao filho como instrução de próxima sessão", linha=n, grupo="pendencia")
                continue
            bruto = limpo(v).lower()
            if nomecol in VOCAB_MULTIPLO:
                partes = [re.sub(r"\s*\(.*?\)", "", p) for p in re.split(r"\s*[·+]\s*|\s+e\s+", bruto)]
            else:
                partes = [re.sub(r"\s*\(.*$", "", re.split(r"\s+[·—]\s+", bruto)[0])]
            if not all(any(casa(p.strip(" ."), o) for o in opcoes) for p in partes):
                falhas.append((n, ident, limpo(v)))
            total += 1
        sistematico = len(falhas) >= 3 and len(falhas) * 2 >= total
        if sistematico:
            rel.add("medio", 4, nome,
                    f"{ch}: coluna '{nomecol}' fora do vocabulário do template ({' / '.join(opcoes)}) em {len(falhas)} de {total} linhas "
                    f"({falhas[0][1]}–{falhas[-1][1]}; ex.: '{falhas[0][2][:40]}') — desvio sistemático: um passe com o aluno, não linha a linha",
                    linha=falhas[0][0], grupo="vocabulario")
        else:
            for n, ident, v in falhas:
                rel.add("medio", 4, nome,
                        f"{ch} {ident}: '{nomecol}' = '{v[:50]}' fora do vocabulário do template ({' / '.join(opcoes)}) — a escolha é do aluno",
                        linha=n, grupo="vocabulario")

    # pendência fora das colunas de vocabulário (ex.: carga dominante no 1.4)
    for ch, tabs in doc.tabelas.items():
        t = tabs[0]
        vcols = {norm_cab(nc_) for (cc, nc_) in tpl["vocab"] if cc == ch}
        for n, l, c in t["dados"]:
            for k, v in enumerate(c):
                if k < len(t["cab"]) and norm_cab(t["cab"][k]) in vcols:
                    continue
                if PENDENCIA.search(v):
                    cab_k = t["cab"][k] if k < len(t["cab"]) else f"col {k+1}"
                    rel.add("medio", 4, nome, f"{ch} {limpo(c[0])[:20]}: '{cab_k}' com pendência ('{PENDENCIA.search(v).group(0)}') — devolver ao filho", linha=n, grupo="pendencia")

    # --- 5. placar -------------------------------------------------------------
    if t14 is not None and t12 is not None:
        entradas = []
        for _, _, c in d12:
            pd = parse_data(valor(t12, c, "Data") or "")
            ver = limpo(valor(t12, c, "Veredito") or "").lower()
            entradas.append((pd, ver, limpo(c[0])))
        for n, l, c in d14:
            res = valor(t14, c, "Resultado") or ""
            vol = valor(t14, c, "Volume") or ""
            pd = parse_data(valor(t14, c, "Data") or "")
            rotulado = re.search(r"(\d+)\s+acertos?\D{0,40}?·\s*(\d+)\s+erros?\D{0,40}?·\s*(\d+)\s+qualificad", limpo(res))
            m = re.search(r"\*\*(\d+)\s*/\s*(\d+)\s*/\s*(\d+)\*\*", res) or rotulado
            if not m:
                continue
            a, e, q = map(int, m.groups())
            ident = limpo(valor(t14, c, "Data") or "")[:30]
            nums_vol = [int(x) for x in re.findall(r"\b(\d+)\b", limpo(vol))]
            if nums_vol and a + e + q not in nums_vol:
                rel.add("medio", 5, nome, f"1.4 {ident}: placar {a} / {e} / {q} soma {a+e+q}, o volume diz '{limpo(vol)[:60]}'", linha=n)
            if not pd:
                continue
            no_periodo = [(v, i) for d, v, i in entradas if d and pd[0] <= d[0] <= pd[1]]
            # acerto registrado é sempre qualificado: acerto limpo não entra no caderno
            # radical, não o termo exato: o vocabulário é conferido na checagem 4,
            # e aqui 'acertei com dúvida' ainda é um qualificado
            q_ent = [i for v, i in no_periodo if v.startswith("acert")]
            e_ent = [i for v, i in no_periodo if v.startswith("err")]
            if len(q_ent) == q:
                continue
            if not rotulado and len(q_ent) == e and len(e_ent) == q:
                novo = l.replace(f"**{a} / {e} / {q}**", f"**{a} / {q} / {e}**", 1)
                rel.add("pequeno", 5, nome,
                        f"1.4 {ident}: placar {a} / {e} / {q} fora da ordem acertos / erros / qualificados — no período há {len(e_ent)} erro(s) ({', '.join(e_ent)}) e {len(q_ent)} qualificado(s) ({', '.join(q_ent)}): {a} / {q} / {e}",
                        linha=n, edicao={"ancora": l, "texto": novo})
            else:
                rel.add("medio", 5, nome,
                        f"1.4 {ident}: {q} qualificado(s) no placar, {len(q_ent)} entrada(s) com acerto registrado no período ({', '.join(q_ent) or 'nenhuma'})", linha=n)

    # --- cobertura do 1.4: toda data de T#/E# cai numa sessão -----------------
    if t14 is not None:
        janelas = [parse_data(valor(t14, c, "Data") or "") for _, _, c in d14]
        janelas = [j for j in janelas if j]
        orfas = {}
        for t, dd in ((t11, d11), (t12, d12)):
            if t is None or col(t, "Data") is None:
                continue
            for _, _, c in dd:
                pd = parse_data(valor(t, c, "Data") or "")
                if pd and not any(j[0] <= pd[0] <= j[1] for j in janelas):
                    orfas.setdefault(pd[0].isoformat(), []).append(limpo(c[0]))
        for d, quem in sorted(orfas.items()):
            rel.add("medio", 5, nome, f"sessão de {d} ({', '.join(quem)}) sem linha no 1.4 — a leitura de evolução é do filho")

    # --- lacuna citando questão sem o E# (heurística) -------------------------
    if t13 is not None and t12 is not None:
        qcol = "Questão (banca/ano/órgão)"
        assinatura = {}
        for _, _, c in d12:
            q = limpo(valor(t12, c, qcol) or "")
            tok = [w for w in re.findall(r"[A-Za-zÀ-ú0-9-]{3,}", q) if not re.fullmatch(r"(item|aula|lista|questão|banca|sem|não|vai|ao|dossiê)", w, re.I)]
            if len(tok) >= 3 and re.search(r"\d{4}", q):
                assinatura[limpo(c[0])] = set(t.upper() for t in tok[:3])
        for n, l, c in d13:
            orig = limpo(c[1]) if len(c) > 1 else ""
            toks = set(t.upper() for t in re.findall(r"[A-Za-zÀ-ú0-9-]{3,}", orig))
            citados = set(re.findall(r"\bE\d+\b", orig))
            for e, sig in assinatura.items():
                if sig <= toks and e not in citados:
                    rel.add("medio", 1, nome, f"1.3 '{limpo(c[0])[:40]}…' cita a questão de {e} ({' '.join(sorted(sig))}) sem o código — heurística: confirmar e glosar (D19)", linha=n)

    # --- 6. citação de arquivo irmão com claude/ ------------------------------
    for i, l in enumerate(doc.linhas):
        if re.search(r"claude/(flashcards|notas-de-melhoria|caderno)-", l):
            novo = re.sub(r"claude/((flashcards|notas-de-melhoria|caderno)-)", r"\1", l)
            rel.add("pequeno", 6, nome, "arquivo irmão citado com o prefixo claude/ (decisão da 1.37: só o nome)", linha=i,
                    edicao={"ancora": l, "texto": novo})

    # --- 7. dossiê -------------------------------------------------------------
    if t21 is not None:
        for n, l, c in d21:
            b = limpo(valor(t21, c, "Banca") or "")
            if not b or b in {"—", "-"}:
                rel.add("medio", 7, nome, f"2.1 com linha sem banca (regra 8 da analise-desempenho): {limpo(l)[:70]}…", linha=n)
    # A contagem da regra consolidada x ocorrências preservadas (2.2) NÃO é
    # conferida: o rastro não tem formato no template (lista com ';', com
    # (i)(ii)(iii), na coluna Regra ou na Ocorrências) e a medição nos quatro
    # cadernos deu falso positivo em formato legítimo. Volta se o template
    # fixar o formato do rastro (D18: medir antes de entrar).

    # --- edição do carimbo ------------------------------------------------------
    edicoes_carimbo = None
    if carimbo is not None and carimbo_fix:
        novo = carimbo
        for r, v in carimbo_fix.items():
            novo = re.sub(rf"(\*\*{re.escape(r)}:\*\*\s*)[^·]*?(\s*(·|$))", lambda m: m.group(1) + v + m.group(2), novo, count=1)
        edicoes_carimbo = {"ancora": carimbo, "texto": novo}

    # estrutura grande absorve o pequeno de estrutura (na dúvida, o balde de cima)
    if estrutura_grande:
        for a in rel.achados:
            if a["arquivo"] == nome and a["grupo"] == "estrutura" and a["balde"] == "pequeno":
                a["balde"] = "grande"
                a["msg"] += " [absorvido pela migração estrutural]"
                a["edicao"] = None
    return {"doc": doc, "carimbo": (carimbo, edicoes_carimbo), "nums_e": nums_e,
            "t_ids": set(ids(" ".join(" ".join(c) for _, _, c in d11) + " " + texto_13, "T")),
            "e_ids": set(nums_e), "max_e": max(nums_e or [0]), "n_f": len(dF)}


# --------------------------------------------------------------------- CSV

def conferir_csv(path, contrato, disciplina, cad, rel):
    nome = Path(path).name
    bruto = Path(path).read_bytes()
    if b"\x00" in bruto[:4096]:
        rel.add("medio", 10, nome, "arquivo binário (fricção 40): não lido — peça o CSV como texto")
        return None
    if bruto.startswith(b"\xef\xbb\xbf"):
        rel.add("pequeno", 8, nome, "UTF-8 com BOM (o contrato pede sem BOM)")
    linhas = bruto.decode("utf-8-sig").split("\n")
    cab = {}
    dados = []
    for i, l in enumerate(linhas):
        if not l.strip():
            continue
        if l.startswith("#") and not dados:
            m = re.match(r"#([^:]+):(.*)$", l)
            if m:
                cab[m.group(1).strip()] = (i, l, m.group(2))
            continue
        dados.append((i, l))
    # 8. contrato
    if contrato is None:
        rel.pular(8, "contrato do CSV não lido da analise-desempenho (passe --analise): checagem pulada, sem valor de reserva")
    else:
        for chave, esperado in contrato.items():
            if chave == "notetype":
                continue  # nome é local à coleção: exato ou omitido, não verificável daqui
            if chave not in cab:
                rel.add("pequeno", 8, nome, f"cabeçalho '#{chave}:' ausente")
                continue
            i, l, v = cab[chave]
            if "<" in esperado:
                continue
            if v != esperado:
                rel.add("pequeno", 8, nome, f"'#{chave}:{v}' — o contrato diz '#{chave}:{esperado}'", linha=i,
                        edicao={"ancora": l, "texto": f"#{chave}:{esperado}"})
        for chave in cab:
            if chave not in contrato and chave != "deck":
                rel.add("medio", 8, nome, f"cabeçalho '#{chave}:' fora do contrato")
    if dados and re.match(r"(?i)\"?(frente|pergunta)\"?\s*[;\t,]", dados[0][1]):
        rel.add("pequeno", 8, nome, "linha de cabeçalho literal vira cartão fantasma (fricção 22)", linha=dados[0][0],
                edicao={"ancora": dados[0][1], "texto": None})
    # 9. linhas
    sep = "\t"
    frentes = {}
    for i, l in dados:
        c = l.split(sep)
        if len(c) != 3:
            rel.add("medio", 9, nome, f"cartão com {len(c)} colunas: {l[:60]}…", linha=i)
            continue
        frente, _, tags = c
        frentes.setdefault(frente.strip(), []).append(i)
        tg = tags.split()
        if not any(t.startswith(disciplina + "::") or t == disciplina for t in tg):
            rel.add("medio", 9, nome, f"cartão sem tag de assunto '{disciplina}::…': {frente[:50]}…", linha=i)
        if not any(t.startswith("tipo::") for t in tg):
            rel.add("medio", 9, nome, f"cartão sem tag tipo::: {frente[:50]}…", linha=i)
        origens = [t.split("::", 1)[1] for t in tg if t.startswith("origem::")]
        if not origens:
            rel.add("medio", 9, nome, f"cartão sem tag origem::: {frente[:50]}…", linha=i)
        for o in origens:
            m = re.fullmatch(r"([TE])(\d+)", o)
            if not m:
                rel.add("medio", 9, nome, f"origem::{o} não aponta para T# nem E#: {frente[:50]}…", linha=i)
            elif cad and int(m.group(2)) not in (cad["t_ids_n"] if m.group(1) == "T" else cad["e_ids"]):
                rel.add("medio", 9, nome, f"origem::{o} não existe no caderno: {frente[:50]}…", linha=i)
    for f, ls in frentes.items():
        if len(ls) > 1:
            rel.add("medio", 9, nome, f"Frente duplicada ({len(ls)}×): {f[:60]} — Frente é chave do Anki, não se reescreve em silêncio (regra 14)", linha=ls[1])
    return len(dados)


# ------------------------------------------------------------------- notas

def triadas(backlog_txt, arquivo_notas):
    """{(N#, data)} já triadas na seção 3 do backlog, pela evidência 'N# de `arquivo`'."""
    out = set()
    sec = backlog_txt.split("## 3.", 1)[-1].split("\n## 4.", 1)[0]
    for l in sec.split("\n"):
        if not l.startswith("|") or arquivo_notas not in l:
            continue
        c = celulas(l)
        if len(c) < 5:
            continue
        d = DATA.search(c[1])
        for nn in re.findall(rf"\b([NM]\d+)(?:,|\s+e\s+[NM]\d+)*\s+de\s+`{re.escape(arquivo_notas)}`", c[4]):
            out.add((nn, d.group(0) if d else None))
        for grupo in re.findall(rf"((?:[NM]\d+(?:,\s*|\s+e\s+))+[NM]\d+)\s+de\s+`{re.escape(arquivo_notas)}`", c[4]):
            for nn in re.findall(r"[NM]\d+", grupo):
                out.add((nn, d.group(0) if d else None))
    return out


def conferir_notas(path, backlog_txt, rel):
    nome = Path(path).name
    doc = Doc(ler(path))
    tabs = [t for ts in doc.tabelas.values() for t in ts]
    if not tabs:
        return
    t = tabs[0]
    ja = triadas(backlog_txt, nome) if backlog_txt else set()
    datas_triadas = {}
    for nn, d in ja:
        datas_triadas.setdefault(nn, set()).add(d)
    for n, l, c in linhas_reais(t):
        ident = limpo(c[0])
        d = DATA.search(c[1]).group(0) if len(c) > 1 and DATA.search(c[1]) else None
        nn = ident
        if re.fullmatch(r"\d+", ident):
            nn = f"N{ident}"
            novo = l.replace(f"| {ident} |", f"| {nn} |", 1)
            rel.add("pequeno", 11, nome, f"nota '{ident}' sem o prefixo N# → {nn}", linha=n, edicao={"ancora": l, "texto": novo})
        elif not re.fullmatch(r"[NM]\d+", ident):
            rel.add("medio", 11, nome, f"nota sem identificador N#: '{ident[:30]}'", linha=n)
            continue
        if backlog_txt is None:
            continue
        if nn in datas_triadas and (d in datas_triadas[nn] or None in datas_triadas[nn]):
            rel.add("pequeno", 11, nome, f"{nn} ({d}) já triada no backlog e ainda no arquivo — podar no filho (fila de saída, D24)", linha=n,
                    edicao={"ancora": l, "texto": None})
        else:
            rel.add("grande", 11, nome, f"{nn} ({d}) nova: triar para a seção 3 do backlog — {limpo(c[3])[:70] if len(c) > 3 else ''}…", linha=n)


# ------------------------------------------------------------------ prompt

def linha_inventario(backlog_txt, caderno_nome):
    sec = backlog_txt.split("### Professores", 1)[-1].split("\n### ", 1)[0]
    for l in sec.split("\n"):
        if l.startswith("|") and caderno_nome in l:
            return l
    return None


def conferir_prompt(path, backlog_txt, cad, caderno_nome, rel):
    nome = Path(path).name
    t = ler(path)
    linhas = t.split("\n")
    m = re.search(r"Vers[aã]o\*{0,2}\s*(\d+\.\d+)", "\n".join(linhas[:6]))
    v_prompt = m.group(1) if m else None
    inv = linha_inventario(backlog_txt, caderno_nome) if backlog_txt else None
    if backlog_txt is None:
        rel.pular(12, "backlog não informado")
    elif inv is None:
        rel.add("pequeno", 12, "backlog-atelie.md", f"professor de '{caderno_nome}' sem linha no inventário")
    else:
        mi = re.search(r"(\d+\.\d+)", celulas(inv)[1])
        v_inv = mi.group(1) if mi else None
        if v_prompt and v_inv and v_prompt != v_inv:
            maior = max((v_prompt, v_inv), key=lambda s: tuple(map(int, s.split("."))))
            if maior == v_prompt:
                rel.add("pequeno", 12, "backlog-atelie.md", f"inventário diz prompt {v_inv}, o arquivo está na {v_prompt} — atualizar o backlog")
            else:
                rel.add("medio", 12, nome, f"prompt na {v_prompt}, o inventário já diz {v_inv} — a base do filho recebeu a versão nova?")
    # 13. envelhecido (heurística: sinaliza, não decide)
    fim = next((i for i, l in enumerate(linhas) if re.match(r"^##\s+Hist", l)), len(linhas))
    vazio_contradito = cad and (cad["max_e"] > 0 or cad["t_ids"])
    for i, l in enumerate(linhas[:fim]):
        if l.startswith("|"):
            continue
        if re.search(r"a confirmar|pend[eê]ncia|pendente|a transcrever", l, re.I):
            rel.add("medio", 13, nome, f"possível texto envelhecido (heurística — conferir no caderno e no backlog): {limpo(l)[:110]}…", linha=i)
        elif re.search(r"est[aá] vazi|nasce vazi", l, re.I) and vazio_contradito:
            rel.add("medio", 13, nome, f"diz que o caderno (ou um bloco) está ou nasce vazio, e o caderno já tem entradas — texto de abertura que pode ter envelhecido (heurística): {limpo(l)[:90]}…", linha=i)
    # 14. teto do D16
    corpo = [l for l in linhas[:fim] if l.strip()]
    if len(corpo) > 60:
        rel.add("grande", 14, nome, f"{len(corpo)} linhas não vazias antes do histórico (teto do D16 ~60): revisar eco no passe de promoção")
    return v_prompt


def conferir_inventario(backlog_txt, caderno_nome, cad, n_cartoes, rel):
    inv = linha_inventario(backlog_txt, caderno_nome)
    if not inv or not cad:
        return
    c = celulas(inv)
    texto = limpo(c[2]) if len(c) > 2 else ""
    m = re.search(r"E1[–-]E(\d+)", texto)
    if m and int(m.group(1)) != cad["max_e"]:
        rel.add("pequeno", 15, "backlog-atelie.md", f"inventário diz E1–E{m.group(1)}, o caderno vai até E{cad['max_e']}")
    m = re.search(r"\((\d+)\s+cart[õo]es\)", texto)
    if m and n_cartoes is not None and int(m.group(1)) != n_cartoes:
        rel.add("pequeno", 15, "backlog-atelie.md", f"inventário diz {m.group(1)} cartões, o CSV tem {n_cartoes}")


# --------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("pasta", help="pasta da disciplina (professores/<disciplina>/) ou onde estão os arquivos")
    ap.add_argument("--template", required=True)
    ap.add_argument("--backlog")
    ap.add_argument("--analise", help="SKILL.md da analise-desempenho (contrato do CSV); procurado se omitido")
    ap.add_argument("--json")
    ap.add_argument("--propor-edicoes", metavar="DIR")
    ap.add_argument("--data", default=date.today().isoformat(), help="data do carimbo nas edições propostas")
    a = ap.parse_args()

    pasta = Path(a.pasta)
    rel = Relatorio()
    tpl = ler_template(a.template)
    analise = a.analise or achar_analise()
    contrato = ler_contrato(analise) if analise else None
    backlog_txt = ler(a.backlog) if a.backlog else None
    if not backlog_txt:
        rel.pular(11, "backlog não informado: cruzamento das notas pulado")

    cadernos = sorted(pasta.glob("caderno-*.md"))
    csvs = sorted(pasta.glob("flashcards-*.csv"))
    notas = sorted(pasta.glob("notas-de-melhoria-*.md"))
    prompts = sorted(pasta.glob("prompt-de-estado*.md"))
    if not cadernos:
        print("sem caderno-*.md na pasta — nada a conferir")
        sys.exit(2)
    caderno = cadernos[0]
    disciplina = caderno.stem.replace("caderno-", "", 1)

    # CSV primeiro só para contar; o cruzamento de origem precisa do caderno
    n_cartoes = None
    if csvs:
        b = csvs[0].read_bytes()
        if b"\x00" not in b[:4096]:
            n_cartoes = sum(1 for l in b.decode("utf-8-sig").split("\n") if l.strip() and not l.startswith("#"))
    cad = conferir_caderno(str(caderno), tpl, rel, n_cartoes, a.data)
    cad["t_ids_n"] = cad["t_ids"]
    if csvs:
        conferir_csv(str(csvs[0]), contrato, disciplina, cad, rel)
    else:
        rel.add("medio", 9, f"flashcards-{disciplina}.csv", "CSV ausente da pasta")
    for nf in notas[:1]:
        conferir_notas(str(nf), backlog_txt, rel)
    if prompts:
        conferir_prompt(str(prompts[0]), backlog_txt, cad, caderno.name, rel)
    if backlog_txt:
        conferir_inventario(backlog_txt, caderno.name, cad, n_cartoes, rel)

    # ------------------------------------------------------------ saída
    print(f"Conferência de {pasta}  ·  template {Path(a.template).name}  ·  "
          f"contrato do CSV: {'lido de ' + analise if contrato else 'NÃO lido'}")
    rotulo = {"pequeno": "PEQUENO — corrige (um 'sim' para o lote)",
              "medio": "MÉDIO — pergunta ao aluno ou devolve ao filho",
              "grande": "GRANDE — backlog"}
    for b in BALDES:
        lst = [x for x in rel.achados if x["balde"] == b]
        print(f"\n== {rotulo[b]}: {len(lst)}")
        for x in lst:
            onde = f"{x['arquivo']}" + (f":{x['linha']}" if x["linha"] else "")
            print(f"  [{x['checagem']:>2}] {onde} — {x['msg']}")
    if rel.notas:
        print("\nNotas (não são achados):")
        for n in rel.notas:
            print(f"  · {n}")
    if rel.puladas:
        print("\nChecagens puladas:")
        for p in rel.puladas:
            print(f"  · [{p['checagem']}] {p['motivo']}")

    if a.json:
        Path(a.json).write_text(json.dumps({"achados": rel.achados, "puladas": rel.puladas, "notas": rel.notas},
                                           ensure_ascii=False, indent=1), encoding="utf-8")

    if a.propor_edicoes:
        destino = Path(a.propor_edicoes)
        destino.mkdir(parents=True, exist_ok=True)
        por_arquivo = {}
        for x in rel.achados:
            if x["balde"] == "pequeno" and x["edicao"]:
                por_arquivo.setdefault(x["arquivo"], []).append(x)
        carimbo, ed_car = cad["carimbo"]
        if carimbo is not None and (ed_car or caderno.name in por_arquivo):
            novo = (ed_car or {"texto": carimbo})["texto"]
            novo = re.sub(r"(\*\*Última atualização:\*\*\s*)\d{4}-\d{2}-\d{2}", rf"\g<1>{a.data}", novo, count=1)
            por_arquivo.setdefault(caderno.name, []).insert(0, {"msg": "carimbo (contagens e data)", "checagem": 1,
                                                                "edicao": {"ancora": carimbo, "texto": novo}})
        for arq, lst in por_arquivo.items():
            eds, vistos = [], set()
            # linha que vai ser podada não recebe outra edição
            podadas = {x["edicao"]["ancora"] for x in lst if x["edicao"]["texto"] is None}
            for x in lst:
                e = x["edicao"]
                if e["ancora"] in vistos or (e["ancora"] in podadas and e["texto"] is not None):
                    continue
                vistos.add(e["ancora"])
                if e["texto"] is None:
                    eds.append({"rotulo": f"[{x['checagem']}] {x['msg'][:60]}", "op": "remover",
                                "ancora_tipo": "linha", "ancora": e["ancora"]})
                else:
                    eds.append({"rotulo": f"[{x['checagem']}] {x['msg'][:60]}", "op": "substituir",
                                "ancora_tipo": "linha", "ancora": e["ancora"], "texto": e["texto"]})
            saida = destino / f"edicoes-{Path(arq).stem}.json"
            saida.write_text(json.dumps(eds, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"\nedições propostas: {saida} ({len(eds)})")


if __name__ == "__main__":
    main()
