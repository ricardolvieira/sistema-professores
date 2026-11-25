# Caderno de Matemática Financeira

> **Última atualização:** 2026-11-23 · **Travamentos:** T0 · **Erros:** E16 · **Linhas no dossiê:** 9 (2.1) + 2 regras consolidadas (2.2) · **Erratas:** F0 · **Cartões:** 1 (em `flashcards-matematica-financeira.csv`) · **Sessões:** 0 teoria / 1 bateria / 0 mista

> Arquivo **vivo** do Project-filho (D14/D25). Quatro naturezas: onde **eu travo** estudando (eixo conteúdo), o que **eu erro** resolvendo (eixo questão), o que **a banca** faz (dossiê) e onde **a fonte** erra (errata).
>
> **Não é material de estudo nem resumo de matéria** — é registro derivado do que eu já enfrentei, seja lendo, seja resolvendo. O caderno existe desde a primeira leitura da disciplina: sem bateria de questões ele registra só o eixo conteúdo, e isso já é indicador (D25).
>
> **Fluxo:** o professor propõe a entrada → eu autorizo → ele grava. **Como** ele grava — snapshot de abertura antes da primeira escrita da sessão, gravação na base deste Project (D28) ou, onde a ferramenta não existir, arquivo em `outputs` para eu subir à mão, releitura de conferência sempre, e os três arquivos vivos entregues como **backup** no fechamento — está na `analise-desempenho`, e só lá. Regra de escrita repetida em dois lugares é regra que diverge (D16).
>
> **Dois arquivos irmãos, mesmo protocolo de escrita (D24).** `flashcards-matematica-financeira.csv` guarda o que é **arbitrário** e precisa de revisão espaçada — não entra aqui em seção nenhuma, porque seu formato é ditado pelo Anki. `notas-de-melhoria-matematica-financeira.md` guarda a **fricção** do professor ou do método, e **esvazia** quando é triada para o backlog do ateliê.
>
> *Instanciado do **template versão 2.1** (2026-09-17) em 2026-11-10. O caderno preenchido versiona por **data de atualização + contagens** — a primeira linha acima é o carimbo que vale; a versão do template é só a linhagem de onde este arquivo saiu.*

---

## Seção 1 — Estado do aluno

> **Dois eixos, duas tabelas, um indicador cada** (D25). O eixo **conteúdo** mede a dificuldade de *entender* — nasce na leitura, sem questão nenhuma. O eixo **questão** mede a dificuldade de *decidir sob pressão* — nasce da bateria. Um não substitui o outro: dá para entender bem e errar na prova, e dá para acertar por reconhecimento sem ter entendido.

### 1.1 Travamentos de conteúdo (eixo conteúdo)

| # | Data | Origem (aula/página) | Tema | O que travou (minhas palavras) | Carga | Destravou com | Reincidência |
|---|---|---|---|---|---|---|---|

*Carga (D2):* **intrínseca** = o assunto é difícil e o texto está claro — o esforço é legítimo e fica. **extrínseca** = a redação é que atrapalha (prolixa, mal sequenciada, convenção não declarada) — a forma se limpa, o conteúdo não. **mista** = limpou-se a forma e ainda restou dificuldade real.

**Critério de admissão — não é diário de perguntas.** Vira T# só o que eu **não teria resolvido sozinho relendo o trecho**: travei, pedi explicação e a explicação era necessária. Curiosidade lateral, pergunta de checagem ("é isso mesmo?") e pedido de exemplo extra não entram. Sem esse corte, a tabela vira transcrição da sessão e perde valor de releitura — é a mesma trava do "não registre acerto limpo" do eixo questão.

**Consolidação:** **três travamentos no mesmo ponto** deixam de ser dúvida pontual e viram **lacuna estrutural** — abre-se a linha em 1.3 com a contagem, e os T# que a formaram são podados daqui (guardando origem e data dentro da lacuna, para a poda ser reversível).

**Leitura do indicador — o que a coluna Carga diz sobre quem tem o problema:** extrínseca dominante num tema é sinal sobre a **fonte**, não sobre mim; se persistir, o destino é a Seção 3 (errata) ou a troca de material. Intrínseca dominante é dificuldade real do assunto e pede tempo, exemplo e questão — não material novo.

### 1.2 Erros em questão (eixo questão)

| # | Data | Questão (banca/ano/órgão) | Veredito | Mecanismo da falha (minhas palavras) | Padrão | Tema | Eixo |
|---|---|---|---|---|---|---|---|
| E1 | 2026-11-11 | Q1 · FCC/2025/SEFAZ PI (ATE-TI) · TEC 3555677 | Acerto com dúvida declarada (D) | A conta eu sabia, mas não consegui interpretar "C, em 1.000 reais" nem ler as faixas com ≤ e < sem ajuda | Leitura do formato do comando (fora do P1–P6) | Juros simples: capital a partir do montante | técnica |
| E2 | 2026-11-12 | Q2 · FCC/2025/CGE PI (Aud Gov-Eng) · TEC 3563360 | Acerto com ajuda (C) | Igualei a soma dos montantes (66.480) só ao M1 e escrevi 0,3 em vez de 0,3·C; não sabia montar capital dividido em partes | Conteúdo | Juros simples: capital fracionado com taxas e prazos diferentes | conteúdo |
| E3 | 2026-11-12 | Q2 · FCC/2025/CGE PI (Aud Gov-Eng) · TEC 3563360 | Acerto com ajuda (C) | Errei a vírgula da taxa (0,12 em vez de 0,012) e travei nos 70% de 60.000: multipliquei por 10 e esqueci de cortar os zeros | Execução aritmética (fora do P1–P6) | Operações com decimais e porcentagem | técnica |
| E4 | 2026-11-12 | Q3 · CEBRASPE/2024/CGE RJ (Aud Est) · TEC 2777820 | Errei (marquei C; gabarito E) | Eu não sabia que "atingir 5 vezes" é o montante: contei os 5C como juros (500% ÷ 10% = 50 meses) em vez de 4C (400% → 40 meses) | Conteúdo | Juros simples: tempo para o capital atingir n vezes | conteúdo |
| E5 | 2026-11-13 | Q4 · FGV/2024/TCE PA (Aud CE) · TEC 3042975 | Acerto com ajuda (E) | Eu sabia que M = C(1 + i·t) sobre os 10.000 por 3 meses não resolvia, mas não sabia como calcular abatendo os pagamentos mensais sobre o saldo devedor | Conteúdo | Juros simples: saldo devedor com pagamentos parciais | conteúdo |
| E6 | 2026-11-13 | Q5 · FGV/2023/Pref RJ (CGM RJ, Cont) · TEC 2368946 | Acerto com dúvida declarada (C) | Não lembrava quantos dias usar para passar a taxa de mês para dia (usei 30) e fiquei em dúvida se contava dezembro como 31 dias | Conteúdo | Juros comerciais × exatos; contagem de dias entre datas | conteúdo |
| E7 | 2026-11-13 | Q6 · FGV/2023/Pref RJ (CGM RJ, TCI) · TEC 2369720 | Acerto com dúvida declarada (D) | Achei i = 0,005 pela fórmula, mas fiquei na dúvida se o resultado já era percentual; não sabia que a fórmula trabalha com a taxa na forma unitária | Conteúdo | Forma unitária × percentual da taxa | conteúdo |
| E8 | 2026-11-13 | Q6 · FGV/2023/Pref RJ (CGM RJ, TCI) · TEC 2369720 | Acerto com dúvida declarada (D) | Me senti inseguro nas divisões e multiplicações com decimais (fiz 5 ÷ 1.000 pela divisão longa, acrescentando zeros); a mesma dificuldade das casas decimais da Q2 (E3) | Execução aritmética (fora do P1–P6) | Operações com decimais e porcentagem | técnica |
| E9 | 2026-11-13 | Q8 · VUNESP/2023/Pref Guararapes (ACI) · TEC 2649741 | Acerto com dúvida declarada (E) | Achei o capital, mas fiquei sem saber por onde ir; tentei usar a diferença dos juros (2.370 − 2.325) e não vi que bastava dividi-la por i·t; resolvi pela fórmula dos juros com o capital novo | Montagem: caminho de resolução (fora do P1–P6) | Juros simples: variação de capital para outro valor de juros | técnica |
| E10 | 2026-11-13 | Q8 · VUNESP/2023/Pref Guararapes (ACI) · TEC 2649741 | Acerto com dúvida declarada (E) | Travei na divisão 17.825 ÷ 1,15; é a terceira vez que a operação com decimais pesa (registros E3 e E8) | Execução aritmética (fora do P1–P6) | Operações com decimais e porcentagem | técnica |
| E11 | 2026-11-14 | Q9 · FGV/2022/SEFAZ ES (Cons TE) · TEC 1888259 | Errei (marquei D; gabarito A) | Não sabia para onde ir: usei o preço inteiro (400) como capital sem descontar a entrada paga no ato, e depois tentei t = 2 contando as duas parcelas | Conteúdo | Juros simples: compra com entrada e parcela única | conteúdo |
| E12 | 2026-11-14 | Q10 · FGV/2021/TCE PI (Ass Adm) · TEC 1695068 | Acerto com dúvida declarada (B) | No início considerei só os 10 dias; depois vi que "após mais 10 dias" soma ao mês que já tinha corrido, total de 40 dias | Leitura do comando (fora do P1–P6) | Juros simples: tempo total × tempo adicional | técnica |
| E13 | 2026-11-14 | Q12 · FCC/2018/TCE RS (APE) · TEC 675492 | Errei (marquei A; gabarito C) | Nunca tinha feito questão de câmbio: multipliquei R por D0 para achar os dólares e dividi por D18 no final, quando era dividir por D0 e multiplicar por D18 | Conteúdo | Juros simples com conversão cambial | conteúdo |
| E14 | 2026-11-14 | Q11 · FGV/2018/Pref Niterói (APPGG) · TEC 632094 | Acerto com dúvida declarada (E) | Quase caí no tempo: ia usar t = 2 meses com a taxa ao bimestre; mudei para t = 1 quando vi que a unidade da taxa era o bimestre | Leitura de unidade (fora do P1–P6) | Juros simples: compatibilizar unidade de taxa e tempo | técnica |
| E15 | 2026-11-16 | Q14 · VUNESP/2018/Pref Guararapes (FOP) · TEC 912320 | Errei (marquei C; gabarito B) | Descontei a entrada do capital (650 − 250 = 400), mas na pressa tratei o total de 682 como montante dos 400, sem tirar a entrada dele; a mesma família da compra com entrada da Q9 (E11), agora só no total | Leitura do comando (fora do P1–P6) | Juros simples: compra com entrada; total com juros × parcela | técnica |
| E16 | 2026-11-16 | Q14 · VUNESP/2018/Pref Guararapes (FOP) · TEC 912320 | Errei (marquei C; gabarito B) | A conta deu 0,3525 e eu marquei 3,5% em vez de ler 35,25%: esqueci de multiplicar por 100; a mesma confusão de forma unitária da Q6 (E7) | Execução aritmética (fora do P1–P6) | Forma unitária × percentual da taxa | técnica |

*Eixo:* **conteúdo** = faltava o conceito (remédio: apostila, via `metodo-professor`). **técnica** = o conceito existia e a leitura escorregou (remédio: procedimento e radar).

**Cruzamento entre as duas tabelas:** erro de eixo *conteúdo* num tema que já tem travamento registrado é reincidência — cite o travamento (glosado, D19) na coluna do mecanismo. É o cruzamento mais informativo do caderno: mostra que a dúvida não foi fechada, só adiada.

### 1.3 Lacunas abertas

| Lacuna | Origem (T# / E#) | Status |
|---|---|---|
| Operações com decimais e porcentagem / casas decimais e forma unitária (× 100) | E3, E8, E10, E16 | aberta: treino de aritmética decimal como frente própria |

**Lacuna com mais de um nome registra os dois desde a abertura.** Quando o mesmo conteúdo aparece na literatura sob nomenclaturas diferentes — edição antiga × edição nova, tradução × original, autor × autor —, a lacuna se escreve com as duas formas (`nome A / nome B`), não só com a que apareceu primeiro. Motivo: lacuna fechada sob um nome continua aberta sob o outro, e a banca cobra pelo que ela quiser. Descobrir o segundo nome só quando ele custa uma questão é caro e evitável — foi assim que uma lacuna dada por estudada reapareceu como erro novo, com outro rótulo.

### 1.4 Registro de sessões

| Data | Tipo | Volume | Resultado | Padrão / tema dominante | Leitura de evolução |
|---|---|---|---|---|---|
| 2026-11-11 a 2026-11-16 | bateria | 15 questões (TEC Q661yr, Meta 02 · T3) | 3 acertos · 8 acertos qualificados · 4 erros (FGV 6, VUNESP 5, FCC 3, CEBRASPE 1) | conteúdo 7 × técnica 9; temas: compra com entrada, unidades de taxa e tempo, decimais | Conteúdo dominou Q2–Q9 (miolo pp. 22–52 não lido); técnica (leitura sob pressa) dominou Q10–Q14; aritmética decimal avançou (Q10, Q13), mas a forma unitária reincidiu (E16) |

*Sessão de **teoria**:* volume = páginas ou tópicos cobertos; resultado = quantos travamentos e qual carga dominou. *Sessão de **bateria**:* volume = questões; resultado = o placar de três parcelas. *Mista:* as duas colunas preenchidas, separadas por `·`.

**Densidade é o indicador do eixo conteúdo:** travamentos por dezena de páginas, comparada entre sessões da mesma disciplina. Número absoluto não diz nada — trinta travamentos em duzentas páginas é outro retrato que trinta em vinte.

---

## Seção 2 — Dossiê de banca

> **Schema de uma linha. Sem narrativa.** Narrativa de erro pertence à Seção 1.
>
> **Consolidação obrigatória:** 3 ocorrências do mesmo mecanismo colapsam em uma **regra** (bloco 2.2), com a contagem, e as linhas individuais são apagadas. Isto é o que impede o caderno de crescer com o número de questões.
>
> **Promoção:** regra estável ao longo de vários ciclos sobe para a skill de disciplina no passe periódico do Project-mãe — e é **podada daqui** depois de promovida.

### 2.1 Ocorrências

| Banca | Ano/Órgão | Formato | Tema | Defeito observado | Padrão |
|---|---|---|---|---|---|
| FCC | 2025/SEFAZ PI | Múltipla escolha (5) | Juros simples: capital a partir do montante | Resposta em faixas de milhar ("C, em 1.000 reais"), alternativas fora de ordem; taxa ao ano com prazo em meses | — |
| FCC | 2025/CGE PI | Múltipla escolha (5) | Juros simples: capital fracionado | Dá a soma dos montantes e pede os juros de uma das partes, não o capital; taxas ao ano com prazos em meses | — |
| CEBRASPE | 2024/CGE RJ | Certo/errado | Juros simples: tempo para o capital atingir n vezes | "Atingir 5 vezes" é montante 5C (juros 4C); o limite do item, 48 meses, fica entre a leitura certa (40) e a que conta 5C como juros (50) | — |
| FGV | 2024/TCE PA | Múltipla escolha (5) | Juros simples: saldo devedor com pagamentos parciais | "Juros sobre o saldo devedor" com dois pagamentos intermediários exige recalcular a cada pagamento; a fórmula única sobre o capital original não chega a nenhuma alternativa; todas as alternativas têm os mesmos centavos (",25") | — |
| VUNESP | 2023/Pref Guararapes | Múltipla escolha (5) | Juros simples: variação de capital para outro valor de juros | Dá o montante e pede quanto o capital deveria ser maior para render um juro dado; exige achar o capital e depois o capital novo (ou dividir a diferença de juros por i·t) | — |
| FGV | 2022/SEFAZ ES | Múltipla escolha (5) | Juros simples: compra com entrada e parcela única | O capital é o preço à vista menos a entrada (200, não 400) e o tempo é 1 mês; o distrator D (20%) é o resultado de usar o preço inteiro como capital | — |
| FCC | 2018/TCE RS | Múltipla escolha (5), alternativas literais | Juros simples com conversão cambial | Dívida em dólar com juros anuais por 18 meses; A inverte as conversões (× D0, ÷ D18); D usa j × 18 sem dividir por 12; B e E são compostos | — |
| FGV | 2018/Pref Niterói | Múltipla escolha (5) | Juros simples: valor original a partir do valor pago com atraso | Taxa dada para o período inteiro (25% no bimestre) com atraso de 2 meses, então t = 1 bimestre; o distrator A (825) subtrai 25% do valor pago em vez de dividir por 1,25 | — |
| VUNESP | 2018/Pref Guararapes | Múltipla escolha (5) | Juros simples: compra com entrada e parcela única | "Valor total da compra, com os juros" (682) inclui a entrada; a parcela é 682 − 250 = 432 e o capital é 400; tratar o total como montante leva a 35% | — |

### 2.2 Regras consolidadas (3+ ocorrências)

| Banca | Tema | Regra | Ocorrências | Promovida? |
|---|---|---|---|---|
| FGV | Juros simples em dias | Taxa mensal convertida em diária pelo mês comercial de 30 dias, informado ou não no enunciado; só a conversão por 30 leva a uma alternativa | 3: 2023/Pref RJ (CGM, Cont), mora 25/11 a 05/12 sem convenção informada, período atravessa a virada do mês · 2023/Pref RJ (CGM, TCI), dá o valor pago com 10 dias de atraso e pede a taxa mensal (× 30 e forma unitária → %) · 2021/TCE PI, "após mais 10 dias" com mês comercial informado, tempo total 40 dias; distrator A capitaliza sobre o montante | não |
| FCC | Juros simples: unidades de taxa e tempo | Taxa dada ao ano com prazo em meses; exige converter (÷ 12) antes da conta, e há distrator para quem não converte | 3: 2025/SEFAZ PI, capital a partir do montante, 10,8% a.a. por 8 meses · 2025/CGE PI, capital fracionado, 12% e 14,4% a.a. por 8 e 10 meses · 2018/TCE RS, empréstimo em dólar, j% a.a. por 18 meses, distrator D usa j × 18 (as três linhas seguem na 2.1 pelos defeitos próprios) | não |

**Perto de consolidar (2 ocorrências — observar a próxima):**
- *(nenhuma)*

Este bloco existe para orientar a observação da próxima sessão: com duas ocorrências não há regra ainda, mas há hipótese. Sem ele, as duplas ficam invisíveis entre a ocorrência solta e a regra fechada.

---

## Seção 3 — Errata da fonte

> **Quarta natureza:** não é estado do aluno nem observação de banca — é **defeito do material de estudo**. Mora aqui, e não em arquivo próprio, pelo mesmo argumento do D14: um segundo artefato vivo por Project é o que faz protocolo ser abandonado na prática.
>
> **Schema de uma linha. Sem narrativa.** Só entra o que foi **conferido** contra fonte de hierarquia superior — edital, lei ou norma vigente, gabarito oficial, comentário da banca (protocolo de fontes da `metodo-professor`). Divergência ainda não confirmada **não** é errata: é dúvida, e vai para *lacunas abertas* (1.3) até fechar.

| # | Data | Onde na fonte (aula/página) | O que a fonte diz | O que é correto — e conforme o quê | Afeta o gabarito? |
|---|---|---|---|---|---|

*Afeta o gabarito?* **sim** = seguir a fonte faz errar questão real; o correto tem de ser decorado por cima. **não** = imprecisão de redação, sem consequência de prova. **só na pegadinha** = a fonte serve na maioria dos casos e quebra no recorte fino que a banca explora — é o caso mais perigoso, porque não aparece enquanto as questões são fáceis.

Uma errata **não** vira regra consolidada nem sobe para skill: ela descreve *este* material, não o campo. Se a mesma fonte acumular erratas no mesmo tema, isso é sinal sobre a fonte — trocar ou complementar o material —, não conteúdo a promover.

**Ponte com o eixo conteúdo:** travamento de carga **extrínseca** não é errata — a fonte está certa, só mal escrita. Errata é a fonte *dizendo coisa errada*. Confundir os dois manda estudar contra a própria fonte primária.

---

## Controle de integridade

Após qualquer escrita: reler o arquivo, conferir **numeração contínua** de T#, E# e F#, **contagem** de travamentos, entradas e erratas, que **nenhuma entrada anterior foi sobrescrita** e que o **carimbo do cabeçalho** (data e contagens, **inclusive a de cartões e a de sessões por tipo**) foi atualizado na mesma operação — só então reportar sucesso. A contagem de cartões do cabeçalho tem de bater com o CSV irmão da última emissão; carimbo que diverge do arquivo é pior que carimbo ausente.
