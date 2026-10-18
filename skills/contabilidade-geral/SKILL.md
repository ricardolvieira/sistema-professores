---
name: contabilidade-geral
description: "Camada de disciplina para Contabilidade Geral, Societária e Avançada em concursos fiscais. Use SEMPRE ao explicar, comentar ou ajudar com qualquer ponto de Contabilidade — patrimônio e variações, escrituração e razonetes, fatos contábeis (permutativo/modificativo/misto), ARE e encerramento, DRE (art. 187 da Lei 6.404/76) e descontos, participações (DEAPF), destinação do lucro e DLPA, DMPL, DFC, DVA, estoques, imobilizado e depreciação, impairment, MEP, consolidação e arrendamento. Funciona JUNTO com metodo-professor (que diz COMO ensinar) e resolucao-questoes (técnica de prova); este skill traz o que é específico de Contabilidade — o estilo de exemplo (razonete em T com D/C explícito, exemplo numérico com números DIFERENTES dos da questão) e o catálogo de pegadinhas por banca (FCC, FGV, CEBRASPE). NÃO cobre Contabilidade Pública nem Análise de Demonstrações — skills próprias. NÃO é material teórico (isso é a apostila); é o mapa de armadilhas."
---

# Contabilidade Geral — camada de disciplina

> **Versão 1.2** · 2026-07-21 · artefato estável (D14)

Use junto com `metodo-professor` (governa o **como**: explicação sob demanda, sem reescrever capítulo, devolvendo à fonte e a uma questão) e com `resolucao-questoes` (governa a **decisão** diante do enunciado). Este skill traz só o que é específico de Contabilidade: como exemplificar, quais instrumentos de rascunho usar e onde a banca arma a cilada. **Não é conteúdo para explicar a matéria — isso é a apostila.**

**Escopo:** Contabilidade Geral, Societária e Avançada (inclusive MEP, consolidação, impairment, arrendamento). **Fora do escopo:** Contabilidade Pública (PCASP, Lei 4.320/64, DCASP) e Análise de Demonstrações (índices, AH/AV, NCG) — skills próprias, ainda não escritas. Se o assunto for um desses, diga que está fora do escopo em vez de improvisar.

## Como exemplificar em Contabilidade

- **O razonete em T é a âncora.** Sempre que o ponto envolver escrituração, encerramento ou efeito no resultado, desenhe o T com **D e C explícitos**. É a técnica preferida do aluno e a que impede conta órfã.
- **Mostre a fórmula em cada linha de cálculo, não só o número.** `Lucro Bruto = Receita Líquida (—) CMV = 180.000 − 116.000 = 64.000`. Número solto não ensina o degrau.
- **Se a pessoa está resolvendo uma questão, o exemplo usa números DIFERENTES dos do enunciado.** Ensina a mecânica sem entregar o gabarito. Regra rígida.
- **Um lançamento-âncora por tema** — aquele lançamento que, entendido, explica os outros do bloco (ex.: em antecipações, o par "pagamento" → "apropriação").
- Amarre ao dispositivo (art. 187 da Lei 6.404/76, CPC correspondente) e devolva a pessoa para reler o trecho com a lente nova.

**Exemplo de exemplo (descontos):** venda de 100.000 com desconto comercial de 10.000 na nota e, depois, desconto financeiro de 2.000 por pagamento antecipado. O comercial é **incondicional** → deduz a receita bruta (RL = 90.000). O financeiro é **condicional** → não toca a receita: entra lá embaixo como **despesa financeira**. Ele *muda de lugar, não desaparece*. Quem "descarta" o desconto financeiro do topo e esquece de trazê-lo de volta erra o lucro líquido — e essa é a armadilha de dois estágios da banca.

## Contabilidade é disciplina de alto suporte (dial)

Contabilidade é declarada de **alta dificuldade** para este aluno. Vale o **dial de suporte** do `metodo-professor`: no comentário pós-tentativa (fase de feedback — o recall já aconteceu, riqueza aqui não fere a trava), o padrão sobe **sem esperar pedido**:

- **Passo a passo sempre explícito:** lançamento completo, nenhum degrau de cálculo pulado.
- **Exemplo numérico como regra**, não como opção.
- **Visual por gatilho, por default** — em Contabilidade o gatilho mais frequente é o próprio lançamento; ver T1 abaixo.

O que o dial **não** muda: o aluno responde **antes** do gabarito, toda explicação devolve à fonte e a uma questão, e nada de varrer capítulo ou gerar material paralelo. O dial regula a profundidade **no ponto**, nunca o escopo.

## Instrumentos de rascunho (técnicas validadas)

Não são teoria: são o que se escreve no papel antes de responder.

- **T1 · Razonete único da ARE.** Varra **todas** as contas de resultado do balancete e jogue cada uma num único T. Saldo credor = lucro; devedor = prejuízo. Preferir isto à DRE em degraus quando o risco é *esquecer uma conta*.
  **T1 não é só rascunho do aluno — é o VISUAL-PADRÃO do comentário pós-tentativa em questão de escrituração.** Sempre que o comentário envolver lançamento (D/C), variação patrimonial por grupo ou fluxo de valores entre contas, renderize o razonete/esquema de caixas no Design System da `recursos-visuais`, **sem esperar pedido**. Um lançamento por esquema. Vale o mesmo para a **linha do tempo** quando a cilada for de momento (competência: pagamento × consumo, venda × entrega).
- **T2 · Teste da equação `ΔA = ΔP + ΔPL`.** Em questão de variação patrimonial: faça o lançamento do período → some por grupo → teste a equação → elimine o que não fecha. Lembre do **duplo lançamento na venda** (receita **e** baixa do estoque), senão o ΔAtivo sai errado.
- **T3 · Escada DEAPF completa, com zero nos degraus ausentes.** **D**ebêntures → **E**mpregados → **A**dministradores → **P**artes beneficiárias → **F**undos de assistência/previdência. Escreva a escada inteira e marque zero onde não houver. Cada participação incide sobre o lucro **remanescente da anterior** (base sucessiva).
- **T4 · Regra do antecipado.** Paguei antes → **ativo** (despesa antecipada). Recebi antes → **passivo** (adiantamento de clientes). Na entrega/consumo, migra para o resultado.
- **T5 · Filtro resultado × patrimonial.** Antes de montar qualquer DRE, risque as contas patrimoniais do balancete (Caixa, Fornecedores, ICMS **a Recolher**, Depreciação **Acumulada**, Veículos, Capital Social). São iscas plantadas.
- **T6 · Duplo sistema, nunca conflagrar.** Sistema A = **fórmula** do lançamento (quantos débitos, quantos créditos). Sistema B = **fato** (permutativo / modificativo / misto → efeito no PL). Se a banca pediu "fórmula", conte as linhas; se pediu "fato", olhe o PL.
- **T7 · Truque do regime.** Quando a banca perguntar sobre um regime, procure nas alternativas a **definição do regime oposto** — ela costuma estar lá. "Fato gerador / competência" × "ingresso de numerário / caixa". *(Instância de **P1 · rótulo trocado** — aplique o tapa-o-rótulo da `resolucao-questoes`.)*

## Como cada banca cobra Contabilidade

O estilo-base de cada banca vive no `metodo-professor`. Aqui, a manifestação específica:

- **FCC** — literalidade da **Lei 6.404/76** e dos CPCs: ordem dos degraus da DRE (art. 187), percentuais (reserva legal, dividendo obrigatório), definições de estoque e de valor recuperável. Alvo predileto: troca de número e de palavra no dispositivo.
- **FGV** — **cálculo aplicado**: dá um balancete ou uma lista de fatos e pede *o valor* de um degrau específico, plantando uma conta que muda de lugar (desconto financeiro, frete sobre venda) ou uma isca patrimonial. Erra quem não varre a lista inteira (usar T1/T5).
- **CEBRASPE** — o formato observado é **múltipla escolha "assinale a correta"** (não certo/errado). A mecânica de ataque está em `resolucao-questoes` (cardápio de defeitos do "assinale a correta": caçar o defeito de cada errada, não a certa). A manifestação contábil recorrente até aqui é **competência × caixa** — ver abaixo. **O acúmulo de casos por banca não mora nesta skill:** vai para a seção *Dossiê de banca* do `caderno-<disciplina>.md` do Project-filho (D14). Sobe para cá só o que consolidar como regra no passe de promoção.

**Núcleo estável — competência × caixa (CEBRASPE):** os dois regimes se definem por **momento de reconhecimento** — fato gerador × ingresso/saída de numerário. Traduza cada alternativa nessa pergunta única: *"segundo esta frase, o que dispara o registro?"* Se a resposta **muda no meio da frase**, é cauda contraditória (a cabeça define competência e o final a condiciona ao caixa) — o defeito mais traiçoeiro do formato. Dois corolários: a alternativa correta costuma ser a **definição limpa** de um dos regimes (frase curta, sem condicional no fim, sem superlativo — sinal a favor, não contra); e vale o **T7**, procurar nas alternativas a definição do regime oposto. Gatilho visual: **linha do tempo com os dois eventos marcados**.

- **FGV e FCC em "assinale a correta"** — sem bloco consolidado. Registre os casos no dossiê do caderno; não extrapole o padrão do CEBRASPE para elas.

## Catálogo de pegadinhas de conteúdo

Cada entrada vem carimbada com o padrão transversal de `resolucao-questoes` (P1 rótulo trocado · P2 absoluto indevido · P4 inversão de mecanismo · P5 generalização com exceção).

### DRE e descontos
- **Desconto incondicional/comercial** (na nota) deduz a receita bruta; **desconto financeiro** concedido (por pagamento antecipado) é **despesa financeira**. Ciladas: deduzir o financeiro da receita bruta [P1]; ou fazê-lo *sumir* da DRE [P4]. **Abatimento** (concedido depois, por defeito/avaria) deduz a receita bruta — chamá-lo de financeiro é [P1].
- **Degraus da DRE (art. 187)**: trocar o rótulo do degrau (Lucro **Bruto** × operacional × antes do IR × **Líquido**) é a pegadinha mais barata da banca [P1]. Ela pede um degrau específico justamente porque o candidato para no primeiro que fecha.
- **Despesa que não consome caixa** (depreciação) reduz o lucro sem reduzir o disponível [P4].

### Fatos contábeis e escrituração
- **Permutativo** não altera o PL; **modificativo** altera; **misto** faz as duas coisas. Cilada: "toda entrada de dinheiro aumenta o PL" — recebimento de duplicata é **permutativo** [P4].
- **Adiantamento de clientes**: no recebimento nasce o **passivo**; na **entrega**, o passivo **morre** e nasce a receita. Marcar "aumento de passivo" na entrega é ver "entrou dinheiro" e não reparar que a obrigação se extinguiu [P4].
- **Contas retificadoras**: Depreciação Acumulada retifica o **ativo** (saldo credor); Capital a Integralizar retifica o **PL** (saldo devedor). Classificá-las como passivo é [P1].
- **Regime de competência**: a receita é do período do **fato gerador**, não do recebimento [P1 — ver T7].

### Imobilizado e depreciação (CPC 27)
- **Custo do ativo** = preço de aquisição **+ todos os gastos para colocá-lo em condições de uso** (frete, seguro no transporte, instalação, montagem). Depreciar sobre o "preço da nota" em vez do custo total é [P4] — o candidato confunde *preço* com *custo contábil do ativo pronto para uso*.
- **Base depreciável** = custo **−** valor residual. Ignorar o residual infla a depreciação [P4].
- A depreciação começa quando o ativo está **disponível para uso**, não quando começa a produzir [P5]. **Terreno não deprecia** [P5].

### DFC (CPC 03) — ponto declaradamente frágil, priorize
- **Método indireto**: parte do lucro líquido e ajusta o que **não** afetou caixa — soma a depreciação, **subtrai** o ganho na venda de imobilizado (que é fluxo de investimento), e ajusta as variações de capital de giro. Somar o ganho ou subtrair a depreciação inverte o mecanismo [P4].
- **Classificação**: compra de imobilizado = **investimento**; empréstimo tomado/amortizado e **dividendos pagos** = **financiamento**; pagamento a fornecedor = **operacional**. Jogar dividendos pagos no operacional é a cilada clássica [P1]. *(O CPC admite classificação alternativa para juros e dividendos — quando o item for específico, confira o dispositivo antes de cravar.)*

### Estoques (CPC 16)
- Mensuração: **menor** entre o **custo** e o **valor realizável líquido (VRL)**. Trocar VRL por "valor justo" ou "valor de mercado" é [P1]; inverter para "maior entre" é [P4].
- **Frete sobre compra** integra o custo do estoque; **frete sobre venda** é despesa [P1]. **Impostos recuperáveis** (ICMS a recuperar) não integram o custo; os **não recuperáveis**, sim [P4].

### Impairment (CPC 01)
- Há perda quando o **valor contábil > valor recuperável**, sendo o recuperável o **maior** entre (a) valor justo líquido de despesas de venda e (b) valor em uso. Dizer "menor entre" é [P4].
- **Reversão de perda por impairment do ágio por expectativa de rentabilidade futura (goodwill) é vedada** — afirmar que se reverte é [P5].

### MEP (CPC 18) e investimentos
- **Coligada** (influência significativa; presunção a partir de 20%) e **controlada** → avaliação pelo **MEP**. Usar o método de custo nesses casos é [P1].
- O resultado de equivalência é a **participação × o lucro do período da investida** — com **pro rata** quando a participação é adquirida ou alienada no meio do exercício. Usar o lucro anual cheio numa operação de 01/07 é [P5].
- **Dividendos recebidos da investida reduzem o valor do investimento**; não são receita [P4].

### Participações e destinação do lucro
- Base das participações: do resultado do exercício deduzem-se **prejuízos acumulados** e a **provisão para o IR** *antes* de qualquer participação (art. 189). Depois, **base sucessiva** pela escada DEAPF — aplicar todos os percentuais sobre a mesma base é [P4].
- **Reserva legal**: 5% do lucro líquido, até 20% do capital social. **Dividendo obrigatório**: se o estatuto for omisso, 50% do lucro ajustado; se fixado sem detalhe, ao menos 25%. Números trocados são o alvo da FCC [P1] — **confira o dispositivo vigente quando o item for de percentual fino.**

## Guardrail de norma volátil

A Lei 6.404/76 e os pronunciamentos do CPC mudam (convergência com IFRS, revisões numeradas). Quando o detalhe for fino — percentual, ordem de degrau, classificação na DFC, redação de um CPC revisado — **mande conferir o dispositivo vigente (ou pesquise) em vez de cravar de memória**. Ensinar regra superada é pior que não ensinar.

## Registro do erro

Quando a pessoa errar uma questão, o diagnóstico é da `resolucao-questoes` (conteúdo × pegadinha). O que cabe **aqui**: nomear o **mecanismo contábil** da falha em uma frase e carimbar o padrão transversal — depois **propor** o registro no `caderno-contabilidade.md` da base de conhecimento do professor, seção *Estado do aluno*. Se o que emergiu foi um **comportamento de banca** (defeito típico, tema recorrente), o destino é a seção *Dossiê de banca* do mesmo caderno, em uma linha (`banca · ano/órgão · tema · defeito · P#`) — não nesta skill. **Nunca regenere um documento de revisão sem autorização explícita**, e nunca gere apostila ou HTML de estudo como resposta padrão a uma dúvida: a entrega é o destravamento pontual, não material novo.

## Lembrete de método

Este catálogo serve para **sinalizar a cilada** enquanto você explica o ponto travado — não para despejar tudo. Aplicado via `metodo-professor`: traduza o nó, desenhe o razonete/exemplo numérico, devolva à fonte. E use a pegadinha relevante para montar a **questão de treino no formato da banca**, que a pessoa responde **antes** do comentário.

## Histórico de versões

| Versão | Data | Mudança |
|---|---|---|
| 1.2 | 2026-07-21 | D14: bloco CEBRASPE reduzido ao núcleo estável, com ponteiro para o *Dossiê de banca* do caderno; FGV/FCC declarados sem bloco consolidado; "Registro do erro" apontando para `caderno-contabilidade.md` (duas seções). |
| 1.1 | 2026-07-21 | Nota 2 do Bloco A: bloco CEBRASPE construído a partir das questões reais (competência × caixa). Remoção do resquício "empilhado para mobile" no T1, contrário ao D13. |
| 1.0 | — | Versão inicial (D12): didática, T1–T7, dial de suporte, catálogo de pegadinhas por tema, guardrail de norma volátil. |
