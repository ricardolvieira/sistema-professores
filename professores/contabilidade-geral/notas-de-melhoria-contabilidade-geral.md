# Notas de melhoria — Contabilidade Geral

> **Artefato vivo** (D24) · **Criado em 2026-09-07** · **1 nota aberta**
> **Natureza: fila de saída.** Este arquivo NÃO acumula. As notas sobem para a seção de fricções do backlog do Project-mãe no fechamento da tarefa e são podadas daqui. Arquivo de fricção que só cresce é acervo.
> Registra o que **o professor ou o método** falharam em entregar — nunca erro do aluno (caderno, Seção 1), da banca (Seção 2) ou da apostila (Seção 3).

---

## M1 · Visual de razonete sem legenda passo a passo é ilegível para quem ainda não domina débito e crédito

**Status:** aberta · **Aberta em:** 2026-09-07 · **Origem:** sessão da aula 04, questão 10 (FGV, ativo circulante com PECLD)

### A fricção

Ao explicar o mecanismo da PECLD, o primeiro visual gerado colocou três razonetes lado a lado (Clientes, PECLD, Despesa) com todos os lançamentos de dois exercícios **colapsados numa única imagem**, sem ordem cronológica declarada e sem explicar o que cada valor representava. Os rótulos ficaram curtos e presos ao lado de cada número ("saldo", "baixa", "complemento"), assumindo que o leitor já saberia reconstituir a sequência.

O aluno respondeu que o visual **não ficou claro** e pediu refação. O razonete só funciona como âncora para quem **já** sabe ler um T; para quem está construindo a mecânica, ele é um amontoado de números em duas colunas.

### O que resolveu

A segunda versão funcionou, e o aluno a indicou explicitamente como modelo. O que mudou:

1. **Eventos numerados** (`1)` a `6)`) dentro do razonete, em ordem cronológica.
2. **Legenda completa abaixo do T**, uma linha por evento, contendo: o que aconteceu no mundo real, o lançamento em D/C, o efeito, e o valor.
3. **Cabeçalho de cada coluna do T dizendo o efeito, não só o lado** — "DÉBITO — aumenta" / "CRÉDITO — diminui" em Clientes; invertido na PECLD, por ser retificadora.
4. **Painel de fechamento** com a regra que explica o conjunto (conta patrimonial carrega saldo × conta de resultado zera).

### Proposta de redação

Para a skill **`recursos-visuais`**, seção do Design System, subseção de razonete — elevar a legenda de opcional a **obrigatória**:

> **Razonete e qualquer visual com lançamento levam legenda passo a passo, sempre.** Numere os lançamentos dentro do T na ordem cronológica e reproduza, abaixo, uma linha por número contendo: (a) o fato do mundo real que disparou o lançamento; (b) o lançamento em D/C com os valores; (c) o efeito — patrimonial ou de resultado; (d) o saldo resultante, quando ele for o ponto. No cabeçalho de cada coluna do T, escreva o **efeito** naquela conta ("DÉBITO — aumenta"), não apenas o nome do lado — a inversão nas retificadoras é justamente o que o aluno ainda não tem automatizado. Na dúvida entre legenda curta e longa, escolha a longa: o custo de uma linha a mais é zero, e o custo de um visual ilegível é a refação inteira.

Para a skill **`contabilidade-geral`**, seção de estilo de exemplo — acrescentar:

> Quando o mecanismo envolver **mais de um momento no tempo** (antecipações, estimativas e sua confirmação, provisões, depreciação, encerramento), não colapse os momentos num visual só. Ou se gera um visual por momento, ou se gera um visual único com os eventos numerados e legendados em ordem. Colapsar momentos é o que transforma razonete em amontoado.

### Por que se paga

O critério do D18 é melhoria que se paga em sessão melhor. Aqui o retorno é direto: **uma refação inteira evitada por visual**. Nesta sessão custou duas rodadas extras — o aluno teve de pedir "não ficou claro" e depois "faça passo a passo" — para chegar num artefato que poderia ter saído certo na primeira. A legenda custa cerca de seis linhas de SVG.

### Evidência anexada pelo aluno

Recorte do SVG `pecld-passo-a-passo-razonetes.svg`, mostrando os dois razonetes com eventos numerados e o bloco "OS SEIS EVENTOS" logo abaixo. O aluno indicou esse formato como o padrão desejado.

---

## Histórico

| Data | Evento |
|---|---|
| 2026-09-07 | Arquivo criado. Nota M1 aberta. |
