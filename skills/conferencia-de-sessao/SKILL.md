---
name: conferencia-de-sessao
description: "Skill operacional do atelie (Project-mae). Use SEMPRE que for conferir, triar ou fechar no atelie a sessao de um Project-filho ja encerrada - caderno, CSV de cartoes, notas de melhoria e prompt de estado - contra o template do caderno, o contrato do CSV e o backlog. Roda o conferidor (scripts/conferir_sessao.py) e separa cada achado em tres baldes: pequeno (mecanico, corrige num lote com um sim do aluno e entrega os integrais), medio (depende de juizo ou da conversa da sessao, propoe o texto e pergunta, ou devolve ao filho como instrucao) e grande (estrutural ou regra de skill descumprida, vai ao backlog). Inclui triar as notas N# e podar as ja triadas. NAO use para gravar registro durante a sessao de estudo, nem para propor entrada, consolidar regra ou promover (isso e da analise-desempenho, no proprio filho), nem para patch de skill ou doc do atelie (entrega-de-artefato, empacotamento-de-skill)."
---

# Conferência de Sessão — o pós-sessão do Project-filho, visto do ateliê

> **Versão 1.0** · 2026-10-22 · skill operacional (D16, D18, D26, D27, D28)

Esta skill não registra nada e não diagnostica nada. Ela confere, **depois** da sessão, o que o Project-filho gravou, e decide o destino de cada defeito achado: corrigir, perguntar ou levar ao backlog.

Existe porque a conferência manual se repetiu seis vezes (backlog 1.32 a 1.47) e quem achou o defeito foi sempre ela, não o professor. A verificação pós-escrita da `analise-desempenho` confere a escrita contra **ela mesma** (numeração, estrutura, diff); não confere contra o **template** nem contra o **vocabulário**. E a lição da fricção 37 vale aqui: checagem descrita no papel não é checagem. Por isso o mecânico mora em **script**, testado contra casos reais.

## Fronteira

| Pergunta | Quem responde |
|---|---|
| O que desta sessão vira registro, e como gravar? | `analise-desempenho`, **no filho, durante** a sessão |
| O que ficou gravado está de acordo com o template, o contrato e o backlog? | **esta skill, no ateliê, depois** da sessão |
| Como sai a versão nova de doc do ateliê ou de prompt de estado? | `entrega-de-artefato` |
| Como sai uma skill? | `empacotamento-de-skill` |

Daqui não sai entrada nova, consolidação, poda de dossiê nem promoção (regra 7 da `analise-desempenho`). O que dependeria disso vai para o balde médio, como instrução ao filho.

**Onde roda:** só no ateliê (decisão de 2026-10-22, backlog 1.48). Chamar o conferidor do fechamento da `analise-desempenho`, no filho, fica para depois de esta skill se pagar em campo, e só com a `analise-desempenho` **apontando** para o script, nunca copiando as checagens.

## Procedimento

1. **Ache os arquivos e o ponto de partida.** No repositório (D27), a pasta é `professores/<disciplina>/`; anote o commit do fechamento (`git log --oneline -- professores/<disciplina>`). Sem repositório, peça os três arquivos vivos e o prompt de estado anexados. Nunca reconstrua arquivo de memória (D26).

2. **Rode o conferidor.** Localize-o em vez de supor o caminho:
   ```bash
   CONF=$(find / -name conferir_sessao.py -path '*conferencia-de-sessao*' 2>/dev/null | head -1)
   python "$CONF" professores/<disciplina> \
       --template atelie/caderno-DISCIPLINA-template.md \
       --backlog atelie/backlog-atelie.md \
       --propor-edicoes ./edicoes --data AAAA-MM-DD
   ```
   O template e o contrato do CSV são lidos **da fonte** a cada execução: o contrato vem da seção *Contrato do arquivo* da `analise-desempenho` (o script procura o `SKILL.md`; passe `--analise` se não achar). Checagem cuja fonte não foi lida sai em *Checagens puladas*, nunca com um valor de reserva.

3. **Leia o relatório e confira o que o script não vê.** A tabela *Cobertura* abaixo diz o que ele confere e o que fica com você. Reclassifique um achado **só para cima**: na dúvida entre dois baldes, vale o de cima (médio antes de pequeno, grande antes de médio). Nunca rebaixe.

4. **Balde pequeno — proponha o lote.** Mostre a lista e rode o `aplicar_edicoes.py` da `entrega-de-artefato` com `--carimbo --simular` sobre cada `edicoes-<arquivo>.json`, para o diff aparecer antes do pedido. Peça **um "sim" para o lote** — não linha a linha, e nunca sem ele. Com o sim, aplique sem `--simular`; se o script reprovar, corrija a edição, não contorne. Nada que exija juízo entra aqui, ainda que pareça trivial (ver *Os três baldes*).

5. **Balde médio — proponha o texto exato e espere.** O que depende da conversa da sessão e o aluno não lembra, devolva ao filho como **instrução de próxima sessão**, numerada, na linha do professor no backlog (precedente: backlog 1.38). Nunca resolva no ateliê o que é do aluno decidir.

6. **Balde grande — leve ao backlog.** Fricção nova ou reincidência de uma registrada, com evidência (arquivo, linha, commit), pela `entrega-de-artefato`. Não corrija aqui o que é estrutural: uma migração malfeita se refaz instanciando o template (fricção 39), não remendando célula.

7. **Notas de melhoria.** N# nova vai para a seção 3 do backlog como fricção (ou como reincidência de uma aberta). N# já triada e ainda no arquivo é **poda**, balde pequeno. O arquivo esvazia; não se exclui (D24).

8. **Antes de entregar ao filho, confira a base dele.** O ateliê não grava na base de outro Project (D28): o caminho é `outputs`, e o aluno sobe à mão. Peça ao aluno que confirme que a base do filho ainda é a versão do commit lido no passo 1. Se não for, a correção foi feita sobre arquivo velho: peça os arquivos atuais e refaça a partir do passo 2.

9. **Entregue os integrais e diga a rota.** Cada arquivo corrigido sai inteiro, com o nome fixo (D27): `caderno-<disciplina>.md`, `flashcards-<disciplina>.csv`, `notas-de-melhoria-<disciplina>.md`. Diga, para cada um, *substituir na base do filho*. Prompt de estado corrigido segue a `entrega-de-artefato` e vai colado nas instruções do Project.

10. **Commite e registre.** Um commit por entrega, com `git diff` antes (D27), identidade só no comando e o push com o arquiteto (`CLAUDE.md` do repositório). A correção do filho é commitada **antes** do upload, e a mensagem diz que ela está *a subir* (precedente 1.38 e 1.47, adotado como regra em 2026-10-22: o repositório registra o que foi entregue, e a conferência do passo 8, na próxima vez, fecha o laço). No backlog, a linha do professor recebe o resultado da conferência e a propagação (fricção 25).

## Os três baldes

| Balde | Critério — todos têm de valer | O que fazer |
|---|---|---|
| **Pequeno** | mecânico; sem juízo diagnóstico; reversível; não muda contagem de regra consolidada (regra 11 da `analise-desempenho`); não muda `Frente` de cartão (regra 14) | aplicar por `aplicar_edicoes.py --carimbo`, com diff, depois de **um sim para o lote**; entregar os integrais |
| **Médio** | depende de diagnóstico ou do que foi dito na sessão — veredito, eixo, carga, cruzamento T × E, banca ausente, mecanismo, sessão sem linha no 1.4 | propor com o texto exato e esperar o aluno; ou devolver ao filho como instrução de próxima sessão |
| **Grande** | estrutural (caderno fora do template), regra de skill descumprida (fricção nova ou reincidência) ou qualquer coisa que toque skill, template ou decisão | não corrigir; registrar no backlog com evidência e commit |

**O caso que calibrou a fronteira entre pequeno e médio.** Na conferência de 2026-10-22, o veredito do E36 de Contabilidade foi trocado no ateliê, junto com as correções mecânicas, de *acertou com lacuna* para *acertou por sorte*. O valor velho estava fora do vocabulário, e isso é mecânico de **detectar**; mas escolher entre *sorte* e *dúvida* é diagnóstico, e a `analise-desempenho` manda não rediagnosticar o que já está registrado. Valor fora do vocabulário é sempre balde médio — o conferidor já o classifica assim.

## Cobertura

O que o conferidor faz, e o que fica na conferência manual. Medido nos casos de aceitação do histórico; o que não foi medido não está marcado como coberto.

| # | Checagem | Script | Balde |
|---|---|---|---|
| 1 | carimbo × conteúdo: T#, E#, F#, dossiê (2.1 + regras da 2.2), cartões × CSV, sessões por tipo, data × última entrada | sim — sessões só em faixa: linha de vários dias ou "(cont.)" não se conta sozinha | pequeno; sessões fora da faixa com linha de vários dias, médio |
| 2 | numeração contínua; lacuna só se declarada (carimbo ou 1.3) | sim | médio |
| 3 | estrutura × template: seções, cabeçalho e ordem das colunas, separador, tabela partida | sim — coluna **local** a mais é aceita (precedente 1.38) e só anotada | grande; título de seção divergente, pequeno |
| 4 | vocabulário de Veredito, Eixo, Carga, Tipo, Status e *Afeta o gabarito?*; células *a transcrever* / *a confirmar* | sim — desvio em mais da metade da coluna sai como **um** achado sistemático | médio |
| 5 | placar: soma × volume; qualificados × entradas *acertou…* do período; ordem | sim — troca só quando erros e qualificados do período casam invertidos | pequeno (troca); médio (resto) |
| — | sessão com T#/E# sem linha no 1.4 | sim | médio |
| — | lacuna citando questão de um E# sem o código (D19) | heurística | médio |
| 6 | arquivo irmão citado com `claude/` | sim | pequeno |
| 7 | linha da 2.1 sem banca | sim | médio |
| 7 | contagem da regra consolidada × ocorrências preservadas | **não** — o rastro não tem formato no template, e a medição deu falso positivo em formato legítimo | conferência manual |
| 8 | contrato do CSV, lido da `analise-desempenho`; BOM; linha de cabeçalho literal | sim — `#notetype:` exato não é verificável daqui | pequeno |
| 9 | três colunas, tags de assunto/tipo/origem, `origem::` existente no caderno, `Frente` duplicada | sim | médio |
| 10 | CSV binário (fricção 40) | sim — avisa e não lê | médio |
| 11 | N# sem prefixo; N# já triada (por N# + data + arquivo na seção 3); N# nova | sim | pequeno; nova, grande |
| 12 | versão do prompt × inventário | sim | médio se o inventário está à frente; pequeno no backlog se atrás |
| 13 | prompt envelhecido: *a confirmar*, *pendência*, *vazio* com caderno cheio | **heurística** — sinaliza, não decide | médio |
| 14 | teto do D16: mais de 60 linhas não vazias antes do histórico | sim; eco de regra de skill **não** | grande |
| 15 | linha do inventário × caderno (E máximo) e × CSV (cartões) | sim | pequeno |
| — | entrada anterior sobrescrita; `Frente` reescrita | **não** — use o `git diff` do commit de fechamento contra o anterior | conferência manual |
| — | mecanismo nas palavras do aluno; acerto limpo registrado; critério de admissão de T# e de cartão | **não** — é juízo | conferência manual, médio |

## Regras inegociáveis

1. **Nada se corrige sem um "sim" para o lote.** Um sim cobre o lote mostrado, não o que for acrescentado depois.
2. **Juízo nunca é balde pequeno.** Veredito, eixo, carga, cruzamento e mecanismo são do aluno, mesmo quando o valor certo parece óbvio.
3. **Na dúvida, o balde de cima.** Reclassificar só para cima.
4. **O script sinaliza; quem decide é a conferência.** Heurística não vira correção sem confirmação.
5. **Sem eco (D16).** Esta skill aponta para as regras da `analise-desempenho` e do template; não as reescreve, e o script as lê da fonte.
6. **O ateliê não grava na base do filho (D28).** Conferir que a base é a versão lida, entregar por `outputs`, o aluno sobe.
7. **Integral, por script, com nome fixo (D26, D27).** Nunca arquivo de edições, nunca arquivo reconstruído.

## Histórico de versões

| Versão | Data | Mudança |
|---|---|---|
| 1.0 | 2026-10-22 | Criação, a partir do handoff da sessão de 2026-10-22 e das seis conferências manuais do backlog (1.32 a 1.47). **Decisões da sessão:** roda só no ateliê; nome `conferencia-de-sessao`; balde pequeno com um "sim" por lote; correção de arquivo vivo pelo `aplicar_edicoes.py` no modo `--carimbo` da `entrega-de-artefato` 1.4; sem D30, porque baldes e fronteira são operação; commit da correção antes do upload, declarado, vira regra (passo 10). **Conferidor** `scripts/conferir_sessao.py`, sem dependência fora da biblioteca padrão, lendo template, contrato do CSV e backlog da fonte. **Aceitação contra o repositório:** Contabilidade `f5e74d7` acha o placar `10 / 2 / 3` fora da ordem (com a troca proposta), o E36 fora do vocabulário **no balde médio**, `#separator:tab`, o prompt 2.3 envelhecido e N1–N3 a podar; aplicadas as edições propostas, o CSV sai idêntico ao de `a7b7497`, e o caderno difere em dois pontos: o E36, que é juízo e ficou de fora de propósito, e a ordem das listas rotuladas na linha do placar, que o conferidor não reordena (troca só os números). Contabilidade `a7b7497`: só N1–N3 a podar, nenhum falso positivo. Tributário `7ee3e70`: caderno fora do template **no balde grande**. Tributário `df8b5d4`: estrutura aceita, com a coluna local; as seis células *a transcrever*/*a confirmar* (Carga de T1–T4, Reincidência do T2, carga dominante do 1.4) no balde médio. RLM `e8475e4`: as quatro inconsistências de 2026-10-12, inclusive a lacuna sem o E25, pela heurística. **Achados verdadeiros que a conferência manual não tinha pego**, nos mesmos casos: Veredito fora do vocabulário em toda a coluna em Tributário (*Marcou × Era*) e em RLM (*errei / acertei com dúvida / acerto qualificado*); Eixo *memorização* (E10) e Status fora da lista em Tributário; `origem::Q14`, `Q24` e `Q27` no CSV de Tributário; o prompt 2.1 de Tributário ainda mandando cumprir a pendência de re-upload que o backlog 1.36 deu por fechada; e, no estado atual, o inventário com 24 cartões de Tributário quando o CSV tem 25. **Fora, por medição:** contagem da regra consolidada × rastro das ocorrências. |
