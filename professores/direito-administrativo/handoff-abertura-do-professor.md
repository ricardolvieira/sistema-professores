# Handoff — abertura do professor de Direito Administrativo

> 2026-11-16 · escrito no ateliê (Project-mãe), no fim de uma sessão longa (fricção 8) · para a próxima sessão do ateliê, com a pasta `D:\dev\pessoal\sistema-professores` conectada

## O que se quer

Montar o Project-filho de **Direito Administrativo** no padrão atual (D16/D24/D25), para rodar a **tarefa 8 da Meta 2**. É a última tarefa da Meta 2 sem professor atual. Diferente dos quatro abertos nesta sessão, é **migração**, não criação: há um professor antigo e uma skill de disciplina com defeito.

Entregável: pasta `professores/direito-administrativo/` com `prompt-de-estado.md`, `caderno-direito-administrativo.md`, `flashcards-direito-administrativo.csv`, `notas-de-melhoria-direito-administrativo.md` e `apostila/<aula>.md`; skill `direito-administrativo` corrigida; commit(s).

## A tarefa 8 (da `claude/meta-2.md`, conferido)

- Material: *Concursos da Área Fiscal — Curso Básico de Direito Administrativo* (Estratégia, 2026, Herbert Almeida e Equipe), **Aula 06**, Atos Administrativos.
- Atividade 1: vícios, mérito e classificação dos atos — pp. 36–49 **do PDF Simplificado**.
- Atividade 2: espécies dos atos, até antes de extinção — pp. 50–59 **do Simplificado**.
- Teoria pura, sem bateria.
- A base usa o **original** (D21): as páginas não vão bater. Traduzir pelo índice do original, como em Constitucional e Português.

## O que falta pedir ao Ricardo

1. **PDF original da Aula 06** de Direito Administrativo (não o simplificado; o script recusa nome com `simplificado`).
2. **As instruções atuais do Project antigo de Administrativo**, se ele quiser aproveitar algo (provavelmente padrão antigo, como os Sniper; ver abaixo).
3. **Dial de suporte:** média ou alta dificuldade. Em Constitucional e Português ficou *média*, a confirmar com ele.

## Estado conferido em 2026-11-16

- Repositório: `main` em `677458f`. Não existe `professores/direito-administrativo/` nem `skills/direito-administrativo/`. Não rastreados, do Ricardo, não mexer: `Claude outputs/` e `professores/contabilidade-geral/caderno-contabilidade-geral-bkp.md`.
- Skill `direito-administrativo` instalada na conta: `SKILL.md` de 84 linhas, **sem linha de versão**, **frontmatter inválido** — o YAML quebra em `mapping values are not allowed here` (linha 3, coluna ~492: dois-pontos dentro da `description` sem aspas). É a **fricção 11**. O conteúdo já cobre atos, e cita a Lei 14.133/2021 e a 8.429/92 com a 14.230/21.
- Backlog do ateliê: **1.48**, de 2026-10-22, **desatualizado** (ver pendências).

## Passos, na ordem

1. **Skill `direito-administrativo` → 1.0 (ou 1.1), pelo L5 e L4 do backlog**, com a `empacotamento-de-skill`:
   - envolver a `description` em aspas duplas (fricção 11);
   - embutir a linha de versão (D15);
   - L4: carimbar as pegadinhas com o tipo transversal P1–P6 e acrescentar o bloco "como este catálogo se lê pelo tipo transversal". Moldes: `direito-tributario` 1.1 e `contabilidade-geral` 1.3. **Não reescrever o catálogo**; mostrar o que mudou e por quê;
   - levar `SKILL.md` e o `.skill` para `skills/direito-administrativo/` (M17).
   - Se o tempo for curto: L5 sozinho já destrava; L4 pode ficar para o próximo toque.
2. **Converter a Aula 06** com a `conversao-apostila`. Começar pela rota pura (é Direito). **Medir antes de aceitar**: cobertura, fragmentação, tabelas, imagens no trecho da tarefa. Nesta sessão a tabela de rota por disciplina errou duas vezes (ver lições).
3. **Caderno:** instanciar do template 2.1 (`atelie/caderno-DISCIPLINA-template.md`). O procedimento é mecânico e foi validado reproduzindo o caderno de LTE byte a byte: trocar título, carimbo (zeros, `0 teoria / 0 bateria / 0 mista`), os dois nomes de arquivo irmão, a linha de linhagem (`(2026-09-17) em <data>`), remover as 7 linhas-exemplo das tabelas, trocar o item de "perto de consolidar" por `- *(nenhuma)*` e cortar o "Histórico de versões do template". Conferir com `diff` contra o caderno de LTE do commit `70d7ff8`.
4. **CSV:** só o cabeçalho do D24, 68 bytes: `#separator:Tab`, `#html:true`, `#columns:Frente<TAB>Verso<TAB>Tags`, `#tags column:3`.
5. **Notas de melhoria:** copiar o de outro professor trocando o nome da disciplina.
6. **Prompt de estado 1.0**, molde `professores/direito-constitucional/prompt-de-estado.md`. Diferenças:
   - **declara a skill de disciplina** `direito-administrativo` (ao contrário dos quatro últimos, que não têm);
   - escopo: Atos Administrativos (Aula 06); fronteira com Constitucional (remédios), Tributário e LTE;
   - fonte primária com a tabela de tradução de páginas e as limitações medidas na conversão;
   - leis voláteis: Lei 9.784/1999 (convalidação, anulação, revogação), Lei 14.133/2021, Lei 8.429/92 com a 14.230/21, súmulas 346 e 473 do STF — conferir com busca, não citar de memória;
   - o caderno nasce vazio; tarefa 8 é teoria pura (só T#).
   - Não reaproveitar texto do professor antigo sem conferir contra D7/D13 (não resolver antes do aluno; sem visual proativo; sem catálogo inventado).
7. **Gravar e commitar** (ver mecânica abaixo). Mensagem no padrão: `adiciona professor de direito-administrativo (prompt de estado 1.0, caderno do template 2.1) (AAAA-MM-DD)`.
8. Lembrar o Ricardo: criar **Project novo** (arquivar o antigo), colar o prompt, subir os 4 arquivos + apostila; instalar a skill corrigida na conta; `git push`.

## Mecânica que custou tempo nesta sessão

- **Git na pasta conectada:** pedir `device_request_delete_permission` **antes** do `git add`, a cada sessão (a permissão não sobrevive). Sem ela ficam `tmp_obj_*` e `.lock` em `.git`.
- **Identidade só no comando:** `git -c user.name="Ricardo Lima Vieira" -c user.email="riclimavieira@gmail.com" commit`. O push é do Ricardo.
- **Cache na gravação:** regravar um arquivo pelo mesmo `stagedPath` mandou a versão antiga ao disco. Ao regravar, usar **caminho novo** em `outputs` e conferir por `sha256sum` nos dois lados antes do commit. `git diff` vazio depois de uma edição é o sintoma.
- **Edição de prompt existente** passa pelo `aplicar_edicoes.py` da `entrega-de-artefato` (com `--versao`), com o commit anterior conferido como ponto de restauração.

## Lições de conversão desta sessão (candidatas a fricção)

- **A rota por disciplina errou nos dois sentidos.** Português (tabela → pura) saiu melhor na **híbrida**: negrito dentro da palavra partia termos (`erudi **ção**`) e uma tabela embaralhou. Matemática Financeira (tabela → híbrida) saiu melhor na **pura**. Não há flag para forçar a híbrida; foi preciso passar `--disciplina "Contabilidade"`.
- **Fórmula em fonte sem texto** (Aula 26): sai como `�`, e a cobertura de vocabulário não acusa. Remédio usado: bloco "OCR de apoio" por página, marcado em comentário HTML.
- **Imagem com conteúdo de estudo** no trecho da tarefa: transcrita à mão, entre comentários `transcrição manual de imagem` / `fim da transcrição`, e declarada no prompt. É a fricção 32 de novo (relatório cego a imagem).
- **Meta cita o Simplificado; a base tem o original:** tabela de tradução de páginas no prompt, sempre.

## Pendências do ateliê acumuladas (não são deste passe; não perder)

O backlog 1.48 não registra nada do que aconteceu desde 2026-10-22:

- **Projects abertos:** Constitucional (C2, `2865d59`, 06/11), Português (C7, `0072cb7`, 09/11), Matemática Financeira (C1, `9b340bf` e `fc6ed6d`, 10/11); prompt de RLM 1.2 (`e88fa48`).
- **Tarefas concluídas da Meta 2:** 12 (LTE), 4 (Constitucional, `a08f278`), 1 (Português), 3 (Matemática Financeira, `677458f`: E1–E16, 2 regras, 1 lacuna, notas N1–N3 **a triar**). A 14 (Contabilidade) estava em fechamento. Resta só a **8**.
- **Fricções novas a registrar:** as três lições de conversão acima.
- **C1 e C6 com dependência satisfeita:** Matemática Financeira e RLM já têm dossiê de banca; as skills podem nascer.
- **Dois Projects Sniper antigos** (Matemática Financeira/Estatística e RLM/Matemática): orientado a arquivar; padrão revogado pelo D13.
- Pasta `professores/raciocinio-logico/` sem `apostila/` (Aula 08), e caderno do repositório em `4cb4ab3` (12/10), a conferir contra a base.
- Dial *média dificuldade* de Constitucional e Português: decisão do assistente, não confirmada.

Fazer o bump do backlog (1.49) pela `entrega-de-artefato`, em passe próprio, depois de Administrativo ou junto com o fechamento da tarefa 14.
