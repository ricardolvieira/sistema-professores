---
name: entrega-de-artefato
description: "Skill operacional de entrega de artefato textual versionado (D26, emenda ao D15; D27 nome fixo; D28 escrita direta). Use SEMPRE que for criar uma versao nova ou patchar documento de base do atelie - documento de decisoes, backlog, template do caderno, mapa do sistema, notas de melhoria, handoff - ou prompt de estado de Project-filho, antes de entregar. Define o fluxo obrigatorio - as edicoes sao metodo interno e nunca entregavel; aplicar com o script aplicar_edicoes.py sobre a copia integra do arquivo, com ancora de casamento unico, verificar versao (--versao; nome fixo), tabelas e diff, e entregar SO o documento completo. Onde a sessao escrever na base, ter restauracao ANTES (commit conferido ou copia), gravar e reler; senao, present_files. Sem o arquivo integro em maos, pedir o arquivo; nunca emitir trecho com instrucao de ancora nem reconstruir de memoria. NAO use para SKILL.md (empacotamento-de-skill), para caderno e CSV de cartoes de Project-filho (analise-desempenho) nem para conteudo de materia."
---

# Entrega de Artefato — integral, nunca arquivo de edições

> **Versão 1.4** · 2026-10-22 · skill operacional (D15, D26, D27, D28)

Esta skill não decide o conteúdo de artefato nenhum. Ela governa **como a versão nova sai**: pronta para substituir a anterior na base, sem montagem do lado de quem recebe.

Existe por causa de um incidente medido. Em 2026-09-11, duas entregas saíram como arquivo de edições (âncora + instrução), com a justificativa "grande demais para entrega integral". As duas foram salvas na base **no lugar** dos documentos íntegros. O custo foi uma semana de registro divergente, uma decisão de estudo tomada com backlog velho, uma sessão parada e dois documentos reconstituídos a partir de conversas. Arquivo de edições *parece* o documento, e é isso que o torna perigoso. O incidente também custou uma segunda coisa, corrigida só no D27: o nome de saída carregava a versão (`<artefato>-vX_Y.md`), então cada versão era um arquivo novo e a anterior só saía de cena se alguém a retirasse à mão — que é exatamente o que não aconteceu.

## Quando disparar

Ao concluir qualquer trabalho cujo produto seja versão nova de artefato textual do ateliê: documento de decisões, backlog, template do caderno, mapa do sistema, notas de melhoria, handoff — e prompt de estado de Project-filho.

**Não** dispare para: `SKILL.md` (a entrega é da `empacotamento-de-skill`; o script desta skill pode ser usado para aplicar as edições, mas a entrega segue aquela), caderno e CSV de cartões (protocolo da `analise-desempenho`), explicação de conteúdo.

**Uma exceção para o script, não para a skill (1.4):** quando o ateliê corrige arquivo vivo de Project-filho no pós-sessão — caderno, CSV de cartões, notas de melhoria —, pela `conferencia-de-sessao`, as edições também passam pelo `aplicar_edicoes.py`, no modo `--carimbo`. A entrega desses arquivos segue aquela skill; daqui vem só o guardrail do D26.

## As quatro proibições

1. **Nunca entregar arquivo de edições.** Nem como anexo "para conferência". A conferência do que mudou vai **na resposta**, em prosa curta; o arquivo entregue é só o integral.
2. **Nunca reconstruir de memória** (fricção 8). Sem a cópia íntegra em mãos, **peça o arquivo** — não emita trecho, não redigite o documento.
3. **Nunca justificar patch por tamanho.** O script aplica as edições sobre o arquivo; o tamanho do artefato nunca passa pela redação.
4. **Nunca gravar na base sem ponto de restauração fora dela.** Gravação direta substitui o documento **no lugar**: no instante em que a nova versão entra, a antiga deixa de existir. O ponto de restauração é a versão anterior entregue ao arquiteto **ou** o commit dela no repositório, **conferido** contra a base (passo 5, M18). Sem um dos dois, o desfazer não existe — e foi exatamente assim que a fricção 34 custou uma sessão inteira de arqueologia de conversa.

## Procedimento

1. **Obtenha a cópia íntegra.** Base do Project (leitura direta, onde a sessão tiver a ferramenta — D28) ou upload. Leia a primeira linha: tem de ser o título do artefato. Se ela anuncia *edições*, *inserção* ou *patch*, pare — é o incidente se repetindo; peça o documento completo.
2. **Escreva as edições** em `edicoes.json` no diretório de trabalho (formato no cabeçalho do script). Prefira âncora de **linha inteira** (`ancora_tipo: linha`); bloco longo vai em arquivo próprio via `texto_arquivo`, nunca escapado dentro do JSON. **Inclua sempre a edição do bump de versão** — o script reprova sem ela.
3. **Rode o script.** Localize-o antes, em vez de supor o caminho. O nome de saída é **fixo** — o mesmo nome do artefato, sem versão — e a versão nova entra por `--versao`:
   ```bash
   SCRIPT=$(find / -name aplicar_edicoes.py -path '*entrega-de-artefato*' 2>/dev/null | head -1)
   python "$SCRIPT" <base> edicoes.json --saida ./<artefato>.md --versao X.Y
   ```
   Se reprovar, corrija a edição e rode de novo. **Não contorne gravando à mão** — a reprovação é o guardrail funcionando.

   **Arquivo vivo de Project-filho** (caderno, CSV de cartões, notas de melhoria) não tem linha de versão: o caderno versiona por carimbo (data e contagens) e os outros dois só pelo commit. Para eles, troque `--versao X.Y` por `--carimbo`. O script reprova se o carimbo do caderno não mudar de data, se `--carimbo` for usado em artefato do ateliê, ou se vier junto com `--versao`. Linha a podar (nota já triada, linha de tabela) sai pela op `remover`, nunca por `substituir` com texto vazio, que deixaria linha em branco dentro da tabela.
4. **Leia o relatório.** O diff tem de mostrar **só** as mudanças intencionais. O script não enxerga semântica: confira à mão o que depende de sentido — contagens declaradas no cabeçalho (itens, fricções), referências cruzadas, números citados em mais de um lugar.
5. **Garanta o ponto de restauração antes de gravar a nova.** Este é o regime do **Project-mãe**, e ele difere do regime do caderno de propósito: aqui a escrita é rara, o artefato é versionado e o que se perde num erro é uma versão inteira mais o elo do histórico. O ponto de restauração é a versão **anterior**, íntegra, tal como foi lida no passo 1 — e ele pode estar em dois lugares (M18):

   - **No repositório, conferido.** Se a sessão enxerga o repositório (D27), confira que o `git log` do caminho mostra o commit da versão lida **e** que o arquivo commitado é igual, byte a byte, ao lido da base (`git show HEAD:<caminho>` contra a cópia do passo 1). Batendo, o commit **é** o ponto de restauração: declare o hash na resposta e siga sem reentregar a anterior.
   - **Entregue ao arquiteto.** Se a sessão não enxerga o repositório, se a versão lida não está commitada, ou se a commitada **diverge** da base, entregue o arquivo da versão anterior antes de gravar — como até a 1.3.

   A dispensa nunca é declaração, é **conferência**: "deve estar no repositório" não dispensa nada. E o motivo da regra não mudou: gravação direta substitui o documento **no lugar**, e sem cópia fora da base o desfazer não existe (fricção 34). O que mudou é só onde a cópia mora quando o M17 já populou o repositório: a 8.11 estava em `71f17b6` e a cópia entregue antes de gravar a 8.12 foi redundante.

   **Fronteira:** isto não toca o regime do **Project-filho**. O snapshot de abertura da `analise-desempenho` continua obrigatório, porque a sessão do filho roda sem o repositório e a equivalência *base = último commit* depende do backup do fechamento anterior (fricção 38).

6. **Entregue o integral.**
7. **Confira pós-escrita (D28), quando a entrega foi direta na base.**
8. **Declare a propagação** (fricção 25):

## O que o script garante e o que não garante

| Garante (reprova e não grava) | Não garante (conferência manual) |
|---|---|
| base íntegra — a primeira linha **anuncia** arquivo de edições (5 primeiras palavras), não apenas contém a palavra | que a base seja a **versão mais recente** |
| cada âncora casa exatamente uma vez | que a edição diga a coisa certa |
| nome de saída sem `edicoes`/`insercao`/`patch`/`delta` **e sem sufixo numérico solto** (`-810`, `-8_10` fora do padrão antigo) | coerência de contagens e referências cruzadas |
| `--versao` (ou versão no header, se o nome ainda a carregar por herança) aparece dentro do documento gerado, e difere da base | histórico de versões redigido |
| nenhuma tabela ganha coluna divergente nem é partida por linha em branco | ordem de seções; se o caminho de saída espelha o repositório (D27) |
| com `--carimbo` (1.4): só arquivo vivo de Project-filho, nunca junto com `--versao`; o carimbo do caderno muda de data; `remover` só com âncora de linha | que a base do filho ainda seja a versão lida (conferência da `conferencia-de-sessao`) |

## Fecho obrigatório

Encerre com uma linha: onde a entrega foi na base do Project, diga que já releu e conferiu (D28) — primeira linha, versão, um único documento no caminho — e diga qual foi o ponto de restauração do passo 5 — o commit conferido (com o hash) ou a cópia da versão anterior entregue, que o arquiteto guarda; onde foi por `outputs`, diga para baixar e subir à mão, retirando qualquer versão anterior com nome versionado que ainda esteja na base. Em ambos os casos, se a primeira linha não for o título do artefato, não sobe.

## Histórico de versões

| Versão | Data | Mudança |
|---|---|---|
| 1.4 | 2026-10-22 | **Duas emendas no mesmo passe, como o backlog pedia.** (1) **M18 — o ponto de restauração do regime do Project-mãe passa a poder ser o repositório.** Passo 5 reescrito: a versão anterior commitada e **conferida** contra a base (o `git log` do caminho mostra o commit da versão lida e o `git show` dela é igual, byte a byte, à cópia lida no passo 1) dispensa a reentrega; sem repositório à vista, sem commit ou com divergência, a entrega volta a ser obrigatória. Quarta proibição e fecho obrigatório acompanham (o fecho declara o hash ou a cópia). Sai o parágrafo *Dois papéis*, cuja premissa — o ponto de restauração "independe de repositório" — o M18 desfez. Motivação: a 8.11 estava em `71f17b6` e a cópia entregue antes de gravar a 8.12 foi redundante. Fronteira mantida: o regime do Project-filho não muda (fricção 38). (2) **Modo `--carimbo` no script, para arquivo vivo de Project-filho corrigido no ateliê.** O caderno versiona por carimbo e o CSV e as notas só pelo commit, então a trava 4 reprovava toda correção — e a de 2026-10-22 saiu por um Python avulso, fora do guardrail (handoff da `conferencia-de-sessao`). Com `--carimbo`: só vale para `caderno-*.md`, `flashcards-*.csv` e `notas-de-melhoria-*.md`; não se combina com `--versao`; exige que o carimbo do caderno mude de data. **Op `remover`** nova, só com âncora de linha, para podar linha de tabela sem deixar linha em branco. Testado com 13 casos: a correção de Contabilidade de 2026-10-22 refeita sobre `f5e74d7` (CSV idêntico ao de `a7b7497`; caderno igual salvo o veredito do E36, que é juízo e ficou de fora de propósito), 9 reprovações (backlog com `--carimbo`, `--carimbo` com `--versao`, carimbo sem data nova, caderno sem `--carimbo`, sufixo `-810`, nome com `edicoes`, `remover` com âncora de trecho, âncora ambígua, separador removido partindo tabela) e a regressão do `--versao` no documento de decisões. **Achado e não corrigido:** os passos 6, 7 e 8 desta skill estão sem corpo na cópia instalada desde a 1.3 — o 8 termina em dois-pontos, sem a lista que anunciava. Não foram reconstruídos de memória (D26); registrados no backlog para recuperar o texto ou reescrever por decisão do arquiteto. |
| 1.3 | 2026-09-17 | **Regime do Project-mãe declarado: a versão anterior é entregue antes de gravar a nova.** O D28 tornou a escrita direta possível, mas gravação no lugar apaga o documento anterior no instante em que o novo entra — e o passe de 2026-09-16 fechou sem nenhum ponto de restauração fora da base. Passo **5 novo** (os demais renumerados para 6, 7 e 8): entregar a cópia íntegra da versão anterior antes da gravação, com os dois papéis separados — **ponto de restauração** (permanente, independe de repositório) e **entrada de histórico** (transitória; em regime estacionário quem entra no repositório é a versão nova, e o resgate da anterior só vale enquanto o M17 não tiver populado o repositório). **Quarta proibição**: nunca gravar na base sem ter entregue a anterior. Fecho obrigatório passa a lembrar da cópia. **Mudança no script, declarada** (a 1.1 já errou ao dizer que não havia): a trava 1 reprovava esta própria skill, cujo H1 termina em *nunca arquivo de edições* — passa a olhar só as **5 primeiras palavras** da linha, pegando quem **anuncia** edições e liberando quem só cita a palavra; testada com 11 casos, 6 de reprovação e 5 de aprovação (**fricção 36**). **Segunda correção no script, mais grave:** a trava de **sufixo numérico solto**, que a 1.2 declarou ter acrescentado e testado, **não existia no código instalado** — `SUFIXO_NUMERICO_SOLTO` não estava lá, e `decisoes-de-design-810.md` voltava a passar; implementada agora e testada com `-810.md` e `-8_10.md` reprovando, nome fixo e o padrão antigo `-vX_Y` aprovando (**fricção 37**: skill e script podem divergir sem que nada acuse, porque o teste da trava roda no papel). Motivação de campo do passe: fricção 34 e o caderno de Direito Tributário zerado em 2026-09-17. |
| 1.2 | 2026-09-16 | Correção da 1.1: a v8.10 do documento de decisões foi entregue como `decisoes-de-design-810.md` — sufixo numérico solto, nome não fixo — e a trava 3 não reprovou, porque só reconhecia `edicoes`/`insercao`/`patch`/`delta` e o padrão antigo `-vX_Y`. `aplicar_edicoes.py` ganha `SUFIXO_NUMERICO_SOLTO`: qualquer saída terminando em `-<dígitos>` (ou `-<dígitos>_<dígitos>`) antes da extensão é reprovada, salvo o padrão antigo mantido por herança. Testado reproduzindo o próprio incidente (reprova `-810.md`), confirmando que o nome fixo com `--versao` passa, e que `edicoes`/`insercao`/`patch`/`delta` seguem barrados. |
| 1.1 | 2026-09-16 | Nome fixo (D27): comando de saída passa a usar `--versao X.Y` em vez de `<artefato>-vX_Y.md`; a trava de nome do script não muda (já aceitava `--versao`), só o exemplo e a tabela de travas. Escrita direta na base (D28): passo 5 bifurca entre gravar direto (com releitura de conferência, passo 6 novo) e `present_files` por outputs, conforme a ferramenta exista na sessão. Fecho obrigatório reescrito para as duas rotas. *Nota corrigida na 1.2: a afirmação "nenhuma mudança no script" era falsa — o gap só apareceu na entrega seguinte.* |
| 1.0 | 2026-09-15 | Criação (D26). Fluxo edições → aplicação por script → verificação → entrega integral; script `aplicar_edicoes.py` com cinco travas, validado reconstruindo a decisões 8.7 byte a byte (md5 igual ao da base) e com doze casos de reprovação, inclusive o do incidente de 2026-09-11; a trava de base íntegra reconhece o frontmatter de `SKILL.md`, defeito pego ao aplicar a `empacotamento-de-skill` 1.4. |
