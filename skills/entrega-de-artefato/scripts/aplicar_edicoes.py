#!/usr/bin/env python3
"""
Aplica uma lista de edicoes sobre a copia INTEGRA de um artefato textual e
grava o documento COMPLETO. O arquivo de edicoes e' metodo interno: nunca e'
entregue (D26, emenda ao D15).

Uso:
    python aplicar_edicoes.py <base.md> <edicoes.json> --saida <arquivo> [--versao X.Y] [--simular]
    python aplicar_edicoes.py <base> <edicoes.json> --saida <arquivo> --carimbo [--simular]

--carimbo (1.4): para ARQUIVO VIVO de Project-filho corrigido no ateliê
(caderno, CSV de cartões, notas de melhoria), que não tem linha de versão:
o caderno versiona por carimbo (data + contagens), o CSV e as notas só pelo
commit. No lugar da trava 4, exige que o carimbo '> **Última atualização:**'
mude de data, quando o arquivo tiver carimbo; sem carimbo, exige que o nome
seja de arquivo vivo. Não se combina com --versao.

Formato de edicoes.json -- lista, aplicada em ordem, cada edicao sobre o
resultado da anterior:
    [
      {"rotulo": "cabecalho",
       "op": "substituir",            # substituir | inserir_antes | inserir_depois | remover
       "ancora_tipo": "linha",        # linha (prefixo de UMA linha inteira) | trecho (substring exata)
       "ancora": "> **Versão 8.7**",
       "texto": "...",                # ou "texto_arquivo": "caminho/para/bloco.md"
      }
    ]
  - substituir + linha  -> troca a linha inteira que comeca com a ancora
  - substituir + trecho -> troca exatamente o trecho
  - inserir_antes/inserir_depois -> exigem ancora_tipo "linha"; inserem o
    texto como linha(s) nova(s) antes/depois da linha ancora
  - remover (1.4) -> exige ancora_tipo "linha" e dispensa texto; tira a linha
    inteira (ex.: nota ja triada, linha de tabela). Substituir por texto
    vazio deixaria linha em branco e partiria a tabela.

Travas (qualquer uma aborta SEM gravar nada):
  1. base nao e' UTF-8 valido, ou a primeira linha denuncia arquivo de edicoes
  2. alguma ancora casa zero ou mais de uma vez
  3. nome de saida contem edicoes/insercao/patch/delta, ou nao carrega versao
     (vX_Y no nome ou --versao)
  4. versao declarada nao aparece no documento (linha "Versao X.Y" no topo
     e/ou primeira linha do historico de versoes), ou nao difere da base;
     com --carimbo: o carimbo do caderno nao mudou de data, ou o arquivo
     sem carimbo nao e' arquivo vivo de Project-filho
  5. tabela Markdown ganhou linha com colunas divergentes ou foi partida
     por linha em branco (bloco de tabela sem linha separadora)
"""

import argparse
import difflib
import json
import re
import sys
from pathlib import Path

PROIBIDO_NO_NOME = re.compile(r"(edi[cç][oõ]es|edicao|inser[cç][aã]o|patch|delta)", re.I)
PROIBIDO_NA_1A_LINHA = re.compile(r"(edi[cç][oõ]es|inser[cç][aã]o\s+cir|patch\b|delta\b)", re.I)
VERSAO_NO_NOME = re.compile(r"-v(\d+)_(\d+)\.[A-Za-z]+$")
# Sufixo numerico solto: '-810.md', '-8_10.md'. Documentado na 1.2 e ausente do
# script instalado ate 2026-09-17 (friccao 37) — a trava que a skill dizia ter
# nunca existiu no codigo, e foi por ela que passou 'decisoes-de-design-810.md'.
SUFIXO_NUMERICO_SOLTO = re.compile(r"-\d+(?:_\d+)?\.[A-Za-z]+$")
VERSAO_TOPO = re.compile(r"Vers[aã]o\*{0,2}\s*(\d+\.\d+)")
LINHA_HISTORICO = re.compile(r"^\| (\d+\.\d+) \| \d{4}-\d{2}-\d{2} \|", re.M)
DATA_CARIMBO = re.compile(r"\*\*Última atualização:\*\*\s*(\d{4}-\d{2}-\d{2})")
ARQUIVO_VIVO = re.compile(r"^(caderno-[a-z0-9-]+\.md|flashcards-[a-z0-9-]+\.csv|notas-de-melhoria-[a-z0-9-]+\.md)$")


def falhar(msg):
    print(f"\nREPROVADO — nada foi gravado.\n  {msg}")
    sys.exit(1)


def ler_utf8(caminho):
    try:
        return Path(caminho).read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        falhar(f"{caminho} não é UTF-8 válido ({e}).")


def primeira_linha(texto):
    """Primeira linha não vazia; em SKILL.md, a primeira depois do frontmatter
    (--- ... ---). Sem isso a trava 1 reprovava skill legítima — defeito pego
    ao patchar a empacotamento-de-skill 1.4."""
    linhas = texto.split("\n")
    if linhas and linhas[0].strip() == "---":
        try:
            fim = linhas[1:].index("---") + 1
            linhas = linhas[fim + 1:]
        except ValueError:
            return "---"  # frontmatter sem fechamento: deixa a trava reprovar
    for linha in linhas:
        if linha.strip():
            return linha.strip()
    return ""


def anuncia_edicoes(l1):
    """A trava 1 pega a linha que ANUNCIA um arquivo de edições, não qualquer
    linha que contenha a palavra. Regra: olhar só as 5 primeiras palavras,
    depois de tirar as marcas de título. Defeito pego ao patchar esta própria
    skill, cujo H1 termina em 'nunca arquivo de edições' e reprovava a si
    mesma (fricção 36)."""
    cabeca = " ".join(l1.lstrip("#").strip().split()[:5])
    return bool(PROIBIDO_NA_1A_LINHA.search(cabeca))


def versao_do_documento(texto):
    """Devolve (versao_no_topo, versao_do_historico) — qualquer uma pode ser None."""
    topo = None
    for linha in texto.split("\n")[:12]:
        m = VERSAO_TOPO.search(linha)
        if m:
            topo = m.group(1)
            break
    hist = LINHA_HISTORICO.search(texto)
    return topo, (hist.group(1) if hist else None)


def aplicar(texto, ed, i):
    rot = ed.get("rotulo", f"edição {i}")
    op = ed.get("op")
    tipo = ed.get("ancora_tipo", "trecho")
    ancora = ed.get("ancora")
    if op == "remover":
        novo = ""
    elif "texto_arquivo" in ed:
        bruto = ler_utf8(ed["texto_arquivo"])
        # remove SÓ a quebra de fim de arquivo (POSIX); rstrip comeria linha
        # em branco intencional no fim do bloco — defeito pego na prova md5
        novo = bruto[:-1] if bruto.endswith("\n") else bruto
    else:
        novo = ed.get("texto")
    if op not in {"substituir", "inserir_antes", "inserir_depois", "remover"} or not ancora or novo is None:
        falhar(f"[{rot}] edição malformada: precisa de op válida, ancora e texto/texto_arquivo.")
    if op != "substituir" and tipo != "linha":
        falhar(f"[{rot}] {op} exige ancora_tipo 'linha'.")

    if tipo == "linha":
        linhas = texto.split("\n")
        idx = [k for k, l in enumerate(linhas) if l.startswith(ancora)]
        if len(idx) != 1:
            falhar(f"[{rot}] âncora de linha casou {len(idx)} vez(es): {ancora[:80]!r}")
        k = idx[0]
        blocos = novo.split("\n")
        if op == "remover":
            del linhas[k]
        elif op == "substituir":
            linhas[k:k + 1] = blocos
        elif op == "inserir_antes":
            linhas[k:k] = blocos
        else:
            linhas[k + 1:k + 1] = blocos
        return "\n".join(linhas)

    n = texto.count(ancora)
    if n != 1:
        falhar(f"[{rot}] âncora de trecho casou {n} vez(es): {ancora[:80]!r}")
    return texto.replace(ancora, novo)


def diagnostico_tabelas(texto):
    """(linhas com colunas divergentes, blocos de tabela sem separador)."""
    blocos, atual = [], []
    for linha in texto.split("\n"):
        if linha.startswith("|"):
            atual.append(linha)
        elif atual:
            blocos.append(atual)
            atual = []
    if atual:
        blocos.append(atual)
    divergentes, orfaos = 0, 0
    sep = re.compile(r"^\|(\s*:?-{3,}:?\s*\|)+\s*$")
    for b in blocos:
        ncol = lambda l: len(re.split(r"(?<!\\)\|", l)) - 2
        ref = ncol(b[0])
        divergentes += sum(1 for l in b if ncol(l) != ref)
        if len(b) < 2 or not sep.match(b[1]):
            orfaos += 1
    return divergentes, orfaos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base")
    ap.add_argument("edicoes")
    ap.add_argument("--saida", required=True)
    ap.add_argument("--versao", help="versão nova (X.Y); obrigatória se o nome de saída não trouxer -vX_Y")
    ap.add_argument("--simular", action="store_true", help="roda todas as travas e o diff sem gravar")
    ap.add_argument("--carimbo", action="store_true",
                    help="arquivo vivo de Project-filho (caderno/CSV/notas): trava de carimbo no lugar da de versão")
    a = ap.parse_args()
    if a.carimbo and a.versao:
        falhar("--carimbo e --versao não se combinam: arquivo vivo não tem linha de versão (D26 com a 1.4).")

    # trava 3 — nome
    nome = Path(a.saida).name
    if PROIBIDO_NO_NOME.search(nome):
        falhar(f"nome de saída {nome!r} descreve arquivo de edições. Entregável é o artefato completo (D26).")
    m = VERSAO_NO_NOME.search(nome)
    if not m and SUFIXO_NUMERICO_SOLTO.search(nome):
        falhar(f"nome de saída {nome!r} termina em sufixo numérico solto. O nome é FIXO "
               "(D27): a versão vai em --versao, na linha do documento, no commit e na tag.")
    versao = a.versao or (f"{m.group(1)}.{m.group(2)}" if m else None)
    if a.carimbo:
        if not ARQUIVO_VIVO.match(nome):
            falhar(f"--carimbo só vale para arquivo vivo de Project-filho (caderno-*.md, flashcards-*.csv, "
                   f"notas-de-melhoria-*.md); {nome!r} não é. Artefato do ateliê versiona por --versao.")
        versao = None
    elif not versao:
        falhar("sem versão: use nome <artefato>-vX_Y.md ou passe --versao X.Y.")
    if m and a.versao and f"{m.group(1)}.{m.group(2)}" != a.versao:
        falhar(f"nome diz {m.group(1)}.{m.group(2)} e --versao diz {a.versao}.")

    # trava 1 — base
    base = ler_utf8(a.base)
    l1 = primeira_linha(base)
    if not l1.startswith("#") or anuncia_edicoes(l1):
        falhar(f"a base não parece o artefato íntegro — primeira linha: {l1[:90]!r}. "
               "Peça o arquivo completo; não aplique edição sobre arquivo de edições.")

    # trava 2 — aplicação
    eds = json.loads(ler_utf8(a.edicoes))
    texto = base
    for i, ed in enumerate(eds, 1):
        texto = aplicar(texto, ed, i)
        print(f"ok   {ed.get('rotulo', f'edição {i}')}")

    # trava 4 — versão (ou carimbo, no arquivo vivo)
    b_topo, b_hist = versao_do_documento(base)
    if a.carimbo:
        b_c, s_c = DATA_CARIMBO.search(base), DATA_CARIMBO.search(texto)
        if b_c and not s_c:
            falhar("a base tem carimbo e a saída não: a edição apagou a linha '> **Última atualização:**'.")
        if b_c and s_c.group(1) == b_c.group(1):
            falhar(f"carimbo continua em {b_c.group(1)}: faltou atualizar a data do carimbo junto com a correção.")
        versao = f"carimbo {s_c.group(1)}" if s_c else "sem carimbo (arquivo vivo; versiona pelo commit)"
    else:
        s_topo, s_hist = versao_do_documento(texto)
        achadas = [v for v in (s_topo, s_hist) if v]
        if not achadas:
            falhar("o documento não declara versão (nem linha 'Versão X.Y' no topo, nem histórico).")
        if any(v != versao for v in achadas):
            falhar(f"versão declarada {versao}, documento diz topo={s_topo} histórico={s_hist}.")
        if versao in (b_topo, b_hist):
            falhar(f"a base já está na {versao}: faltou o bump de versão.")

    # trava 5 — tabelas
    b_div, b_orf = diagnostico_tabelas(base)
    s_div, s_orf = diagnostico_tabelas(texto)
    if s_div > b_div:
        falhar(f"linhas de tabela com colunas divergentes: {b_div} -> {s_div}.")
    if s_orf > b_orf:
        falhar(f"blocos de tabela sem linha separadora: {b_orf} -> {s_orf} (linha em branco partiu tabela?).")

    # relatório
    bl, sl = base.split("\n"), texto.split("\n")
    cab = lambda ls: sum(1 for l in ls if l.startswith("#"))
    if a.carimbo:
        b_c = DATA_CARIMBO.search(base)
        print(f"\ncarimbo      : {b_c.group(1) if b_c else '—'} -> {versao}")
    else:
        print(f"\nversão       : {b_topo or b_hist} -> {versao}")
    print(f"linhas       : {len(bl)} -> {len(sl)}")
    print(f"cabeçalhos # : {cab(bl)} -> {cab(sl)}")
    print(f"tabelas      : divergentes {b_div} -> {s_div} · sem separador {b_orf} -> {s_orf}")
    print("diff (só mudanças intencionais devem aparecer):")
    sm = difflib.SequenceMatcher(a=bl, b=sl, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        print(f"  {tag:<8} base {i1+1}-{i2} -> saída {j1+1}-{j2}  (-{i2-i1} +{j2-j1})")
        for l in sl[j1:j2][:2]:
            print(f"      + {l[:100]}")

    if a.simular:
        print("\nSIMULAÇÃO — travas passaram, nada gravado.")
        return
    Path(a.saida).parent.mkdir(parents=True, exist_ok=True)
    Path(a.saida).write_text(texto, encoding="utf-8")
    print(f"\nAPROVADO — gravado o integral: {a.saida}")


if __name__ == "__main__":
    main()
