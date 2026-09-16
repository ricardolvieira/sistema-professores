# Decisões de Design — Sistema de Professores de Estudo

> **Versão 8.10** · 2026-09-16 · artefato **estável** (D14/D17). Alterações desde a v8.9: **D27** — corrigido o caminho do repositório (`D:\dev\pessoal\sistema-professores`, pasta local não sincronizada, confirmada pelo arquiteto) e explicitado que é **um único repositório para o sistema inteiro** — ateliê e todos os Projects-filhos —, nunca um por professor; acrescenta a convenção de espelhamento de caminho entre repositório e base.
 
> Registro do **que** foi decidido e **por quê**. Serve para o meta-trabalho (melhorar skills e prompts) não virar arqueologia de conversa. Quando bater a dúvida "por que é assim?", a resposta está aqui.
 
## Arquitetura em uma frase
 
**Project-mãe** (este ateliê: projeta e mantém a camada de cima) → **skills** (o cérebro compartilhado, da conta inteira) → **Projects-filhos** (os professores, onde de fato se estuda, cada um com a apostila da sua matéria).
 
A inteligência mora nas **skills**, não nos prompts. Atualiza-se uma skill uma vez e todos os professores melhoram. Os prompts dos professores são **magros**: persona da disciplina + "use suas skills" + apostila como fonte + banca-alvo.
 
## Princípios invioláveis
 
- **A trava:** andaime, não reescrita. Explicar o ponto travado sob demanda, manter o livro original (denso) como leitura primária, e sempre devolver à fonte e a uma questão. Nunca pré-mastigar o capítulo.
- **Carga intrínseca × extrínseca:** preservar o esforço da dificuldade do *assunto* (intrínseca); limpar a dificuldade da *redação ruim* (extrínseca). Limpar forma ruim não é trapaça — é dar acesso à dificuldade real.
- **Prática no formato da prova:** verificação é uma questão real da banca, respondida *antes* do comentário (recall, não reconhecimento).
- **Fidelidade inegociável:** não inventar fato/artigo/súmula; exemplos ilustram, não adicionam conteúdo cobrável; verificar leis voláteis com busca quando o tema muda.
- **Não reintroduzir a postura "otimização-primeiro":** nada de visual proativo varrendo o tópico, nada de "carga extrínseca zero". Skills enxutas.
 
## Decisões
 
### D1 — Andaime, não reescrita
**Contexto:** a tentativa anterior (GEM de otimização) gerava material liso que dava *sensação* de aprendizado, mas falhava na hora das questões.
**Decisão:** o professor destrava o ponto específico sob demanda; não reescreve apostila.
**Por quê:** a fluência (facilidade de ler) é confundida com entendimento. O esforço no estudo é o que cria memória recuperável, e a prova cobra decodificar texto denso e capcioso. Texto pré-mastigado treina a habilidade errada.
 
### D2 — Separar carga intrínseca de extrínseca
**Contexto:** risco de a trava ficar ampla demais e "proteger" também a redação ruim do material.
**Decisão:** diagnosticar *por que* travou. Intrínseca (assunto difícil, texto claro) → manter o esforço. Extrínseca (redação prolixa/mal sequenciada) → reestruturar *aquela passagem* sem diluir o conteúdo. As duas → limpar a forma primeiro, depois aplicar o esforço.
**Por quê:** ruído de redação não é dificuldade desejável. Era essa confusão que motivava a vontade de regerar a apostila.
**Mecanismo:** atalho do aluno — "reestrutura isso" força o modo extrínseco; "não facilita, só destrava" força manter o esforço.
 
### D3 — Inteligência nas skills, não nos prompts
**Decisão:** o que é reutilizável vira skill (fonte única, versionável); o prompt do professor só *referencia* as skills.
**Por quê:** evita professores inchados em série e o problema de manutenção (inteligência congelada dentro de cada prompt fica desatualizada). Atualizar a skill melhora todos de uma vez.
**Adendo (ver D16):** "magro" nunca foi métrica de tamanho. O critério é a **portabilidade** — o que faria sentido em qualquer professor é inteligência (skill); o que só faz sentido neste é estado (prompt). O nome canônico passa a ser **prompt de estado**.
 
### D4 — Três camadas de skill
**Decisão:** **universal** (`metodo-professor` = como ensinar) + **por disciplina** (estilo de exemplo + catálogo de pegadinhas + manifestação da banca) + **visual** (`recursos-visuais` = Design System + catálogo de diagramas).
**Por quê:** ortogonalidade. A universal cuida do *como*; a de disciplina, do que é específico do campo; a de visual, da forma padronizada. Cortar onde o *método de ensino* muda (ex.: Matemática Financeira pede exemplo numérico, não analogia).
**Adendo (ver D11):** a camada **universal** passou a conter **duas** skills ortogonais — `metodo-professor` (como ensinar / compreensão) e `resolucao-questoes` (técnica de prova / decisão). As três *camadas* seguem as mesmas (universal, disciplina, visual); o que mudou é que a universal agora tem duas skills, cortadas onde o eixo muda (compreender conceito × decidir questão).
 
### D5 — Banca: estilo-base no universal, manifestação na disciplina
**Contexto:** dois prompts antigos (Administrativo e Contabilidade) traziam a mesma tabela genérica de bancas.
**Decisão:** o estilo-base de FCC/FGV/CEBRASPE vive no universal; cada skill de disciplina guarda só a manifestação específica (quais leis/temas cada banca enfatiza naquele campo).
**Por quê:** elimina duplicação. A tabela genérica idêntica nos dois prompts era o sinal de que era material universal.
 
### D6 — Mineração de sinais + protocolo de priorização no universal
**Decisão:** garimpar os sinais que o autor já deixou na fonte ("cai muito", "cuidado", coruja) e sinalizar a origem; e seguir a hierarquia de fontes **anexos > edital > fallback com busca**.
**Por quê:** ambos vieram dos prompts antigos, são cross-disciplina e reforçam a trava (devolver à fonte) e a fidelidade.
 
### D7 — Prática em questões reais é o produto; clarificação é andaime
**Decisão:** o centro de gravidade do estudo é fazer questões no formato real da banca; a explicação clarificadora é suporte pontual.
**Por quê:** "ir bem nas questões" é uma habilidade de *fazer questões*. Os fluxos antigos descartavam as questões comentadas (o ativo mais valioso) e tratavam só nomes de tópico ou frequência.
 
### D8 — Fidelidade e leis voláteis
**Decisão:** acurácia acima de tudo; quando o tema for de área que muda (Reforma Tributária — IBS/CBS/IS; Licitações 14.133; Improbidade 14.230), verificar o estado atual com busca antes de cravar.
**Por quê:** ensinar regra superada é pior que não ensinar. As skills de disciplina mandam conferir o dispositivo vigente quando o detalhe é fino.
 
### D9 — O que se aproveitou e o que se cortou do material antigo
**Aproveitado** dos GEMs e dos prompts de professor: fluxo de intake, localização por páginas, inventário de "ativos de alto valor", lógica de camadas/fusão (🚨🔥🔎), o princípio diagnóstico de visual (estrutura → tipo de diagrama), calibração-antes-de-prosseguir, tabelas de banca e o Design System.
**Cortado:** a cerimônia teórica (nomes de ADDIE/Gagné/TCAM e chain-of-thought performático) e, sobretudo, o telos de "carga extrínseca zero" / otimização-primeiro.
 
### D10 — Logística no claude.ai
**Decisão:** as skills personalizadas são da **conta** (sobem uma vez — botão "Salvar habilidade" no chat, ou zip com a pasta na raiz em Configurações) e disparam por relevância. Os professores são **Projects** com a apostila em `.md` na base de conhecimento.
**Por quê:** sobe a inteligência uma vez; cada professor vira "casca + apostila". O Project-mãe é o ateliê das skills/prompts; os Projects-filhos são onde se estuda.
 
### D11 — Técnica de prova é skill própria, irmã da `metodo-professor`
**Contexto:** a prática de questões já era princípio (D7), mas morava difusa — parte em "Treine no formato da prova" na `metodo-professor`, parte implícita. Uma sessão de resolução de ~20 questões fez emergir padrões estáveis (radar de pegadinha, procedimento de decisão, diagnóstico conteúdo × pegadinha) grandes demais para caber como módulo.
**Decisão:** criar a `resolucao-questoes`, universal, ao lado da `metodo-professor`. Divisão de eixo — `metodo-professor` = compreensão do conceito ("o que isso significa?"); `resolucao-questoes` = decisão sob pressão diante do enunciado ("o que este item afirma, e onde está a cilada?").
**Por quê:** são perguntas diferentes com entregas diferentes (destravar conceito × procedimento + diagnóstico). Fundir incharia a `metodo-professor` e violaria a ortogonalidade de D4. É o D7 ("prática é o produto") ganhando casa própria.
**Fronteira:** o catálogo de **forma** (transversal, P1–P6) + procedimento + diagnóstico ficam na skill nova; os catálogos de **conteúdo** seguem nas skills de disciplina, conectados por *tipo, não por cópia* (a skill nova dá o rótulo do padrão; a de disciplina, o caso concreto). A `metodo-professor` mantém a verificação como fecho da explicação e aponta para a skill nova via gancho.

### D12 — Contabilidade cortada em três; mapa de erros é estado, não disciplina
**Contexto:** o Estado atual registrava uma única `contabilidade` ("extrair do prompt SNIPER"). O handoff do Professor Sniper mostrou que o material real separa naturalmente em blocos que se ensinam por métodos diferentes, e que o histórico do aluno é um log de erros que cresce toda semana.
**Decisão:** três skills de disciplina — `contabilidade-geral` (inclui societária e avançada: MEP, consolidação, impairment, arrendamento), `contabilidade-publica` e `analise-demonstracoes`. Só a primeira nasce agora; as outras quando houver histórico de estudo. O **mapa de erros do aluno** (E1…En) vive na **base de conhecimento do Project-filho**, não na skill.
**Por quê:** corte por método do D4. Geral/Societária/Avançada se ensinam por **lançamento, razonete e número**; Pública, por **norma orçamentária e literalidade da 4.320**; Análise, por **índice e interpretação**. Um `contabilidade` monolítico diluiria as três didáticas. Quanto ao mapa de erros: é **estado do aluno** (volátil, pessoal, de uma matéria), não **conteúdo de disciplina** (estável, de todos). Pôr o log dentro de uma skill misturaria as duas naturezas, forçaria re-upload a cada erro e vazaria dado pessoal para a camada compartilhada da conta (contra D3/D10). A skill guarda só o **protocolo** de nomear o mecanismo e carimbar o padrão P1–P6; o caso concreto fica no project — é o "elo por tipo, não por cópia" do D11.
**Gatilho de revisão:** se um dia o histórico de erros passar a atravessar disciplinas (mesmo padrão em Contabilidade e em Tributário), reconsiderar um caderno de erros **único e transversal na conta**. Não é o caso hoje (histórico 100% Contabilidade).

### D13 — A trava limita escopo e momento, não profundidade
**Contexto:** o primeiro test-drive do professor de Contabilidade saiu telegráfico e quase sem visuais. A comparação com o professor antigo (Sniper) mostrou que o corte da cerimônia (correto, D9) e da resolução-antes-do-aluno (correto, D7) levou junto algo que não devia: a riqueza do comentário pós-tentativa. Causas: (a) as skills aplicavam a contenção da trava também à fase de feedback; (b) `recursos-visuais` só tinha freio ("nunca proativo", "confirmar custo") e nenhum acelerador — além de uma premissa "mobile-first" herdada do Sniper que não corresponde ao uso real (o aluno estuda em tablet e PC); (c) o prompt magro traduziu "legível no celular" como "resposta curta".
**Decisão:** três distinções passam a ser explícitas nas skills. **Tentativa × feedback** — a trava protege o esforço *antes* da tentativa (não pré-mastigar, não antecipar, recall antes do gabarito); *depois* da tentativa, o comentário pode ser tão profundo quanto o ponto exigir, incluindo visual por gatilho sem pedido. **Profundidade × amplitude** — "parar" é não expandir para conceitos vizinhos, não ser raso ou telegráfico no ponto em questão. **Dial de suporte** — o prompt do Project-filho pode declarar a disciplina como de alta dificuldade para o aluno (Contabilidade, Matemática Financeira, RLM…), elevando o padrão: passo a passo sempre explícito, visual por gatilho como default, exemplo numérico como regra. A confirmação de escopo/custo fica restrita a artefatos grandes (HTML interativo, documento multipágina) — nunca a diagrama/esquema inline. **Postura de `recursos-visuais`: abundância, não parcimônia** — a prioridade é o aprendizado; dentro de explicação/comentário, gatilho presente = gera por padrão, sem racionar por custo. As únicas proibições são varredura (proativo cobrindo capítulo) e decoração (enfeite sem carga didática). A premissa "mobile-first" foi removida (o aluno usa tablet e PC): visuais podem usar layout amplo, sem restrição de largura.
**Por quê:** a ilusão de fluência nasce de substituir o esforço de *codificação*, não de dar feedback claro. Depois do recall, riqueza é ganho líquido — feedback ancorado fixa o mecanismo certo. O professor antigo errava resolvendo antes do aluno (isso não volta); o novo errava sendo telegráfico depois. O dial existe porque a profundidade-padrão ideal varia por aluno × disciplina, e essa informação é estado do Project-filho (como o mapa de erros do D12), declarada no prompt magro.
**Mecanismo:** `metodo-professor` (seção "Tentativa × feedback" + "Dial de suporte" + passo 4 reescrito como "pare de expandir, não de aprofundar"); `recursos-visuais` (seção "Quando gerar" com duas fronteiras — proibido só varredura/decoração, resto por padrão sem racionar; gatilhos novos de decomposição numérica/razonete e dois-momentos-no-tempo; regra 1 "Aprendizado > economia"; premissa mobile removida, layout amplo liberado para tablet/PC; custo restrito a artefato grande); `resolucao-questoes` (seção "Anatomia do comentário pós-tentativa" + regra inegociável 5); prompts magros (linha do dial + "abuse de recursos visuais" nas disciplinas difíceis).
**Fronteira:** o dial não reabre a otimização-primeiro. Continua proibido: varrer capítulo, gerar material paralelo, visual decorativo, resolver antes do aluno. O dial regula a profundidade do suporte *no ponto*, nunca o escopo nem o momento.
 
### D14 — Artefato estável × artefato vivo; o caderno do project e a skill `analise-desempenho`

**Contexto:** ao implementar o Bloco A das notas de melhoria (sessão de 18/07/2026), o bloco CEBRASPE de `contabilidade-geral` foi escrito **dentro da skill**. O aluno apontou a consequência antes de ela acontecer: o cardápio de defeitos por banca cresce a cada leva de questões, faltam ainda os blocos FGV e FCC, e o mesmo valerá para cada uma das disciplinas. Com skills de conta e `/mnt/project` somente-leitura, isso obrigaria a **regenerar e re-subir uma skill por semana, por disciplina**. O receio declarado foi de ingovernabilidade do conjunto.

**Decisão:** o critério de alocação passa a ser a **frequência de edição**, não só o eixo de conteúdo (que continua valendo, do D4).

- **Artefato estável** — didática da disciplina (como exemplificar, instrumentos de rascunho, dial, guardrails), gramática transversal de pegadinha (P1–P6, cardápios de formato), protocolos. Mora nas **skills** (conta). Edita-se raramente e **em lote**.
- **Artefato vivo** — o que cresce a cada sessão. Mora em **um único arquivo por Project-filho**: o `caderno-<disciplina>.md`, com **duas seções** — *Estado do aluno* (mapa de erros, lacunas) e *Dossiê de banca* (como cada banca cobra cada assunto, acumulado das questões reais).

**Princípio:** *minimizar artefatos **vivos**, não artefatos totais.* Acervo grande e parado é barato; o que custa é o que muda em muitos lugares ao mesmo tempo.

**Por quê:** a skill de disciplina **só dispara dentro do seu próprio Project-filho** — `contabilidade-geral` nunca roda no professor de Redes. Logo, manter a parte volátil no nível da conta não compra reuso nenhum; compra só custo de re-upload. A parte que muda desce para onde é usada. A carga operacional simultânea passa a ser sempre **um project** (o da matéria em estudo), independentemente de quantos existam.

**Terceira natureza (adendo ao D12):** o dossiê de banca não é *estado do aluno* nem *conteúdo de disciplina* — é **observação de campo acumulada**. O D12 previa duas naturezas; esta é a terceira. Não conflita: como as outras duas, é volátil e local, então segue a mesma regra de não morar em skill.

**Arquivo único, não dois:** a fricção de baixar-e-re-subir a cada sessão é o que faz protocolo ser abandonado na prática. Duas seções internas preservam a separação de naturezas com uma operação só. Custo aceito: o arquivo fica grande, e por isso a regra de consolidação abaixo é **obrigatória**, não opcional.

**Anti-inchaço (as três travas do caderno):**
1. **Schema de uma linha** no dossiê — `banca · ano/órgão · tema · defeito observado · padrão P#`. Sem narrativa (narrativa de erro vai para a seção de estado do aluno).
2. **Consolidação por reincidência** — uma ocorrência é registro; **três ocorrências do mesmo mecanismo colapsam em uma regra**, com a contagem. O caderno passa a crescer com o número de **mecanismos distintos** (conjunto finito e pequeno), não com o número de questões resolvidas.
3. **Promoção em passe deliberado** — o que amadurecer como regra estável sobe para a skill num **ritual periódico no Project-mãe** (uma ou duas vezes por ciclo de estudo), nunca continuamente; promovido, é podado do caderno.

Fluxo completo: sessão → fechamento grava no caderno → reincidência consolida em regra → passe periódico promove para a skill.

**Quem escreve:** a **`analise-desempenho`** (Bloco B das notas), e não a `resolucao-questoes`. Esta última é técnica pura — sem estado, sem memória, estável; dar-lhe responsabilidade de escrita a tornaria as duas coisas e quebraria a ortogonalidade comprada no D11. A `analise-desempenho` passa a ser dona do **protocolo de registro em geral**: dois destinos (estado do aluno / dossiê de banca), mesmo mecanismo de captura, mesma autorização explícita antes de gravar, mesma verificação pós-escrita. **Uma skill, um arquivo-alvo, nenhum dado dentro dela** — compatível com o D12. Isso reforça o caso de skill própria: o protocolo é transversal a todos os projects-filhos e não é conteúdo de disciplina nenhuma.

**Requisito herdado do §5 do handoff:** toda escrita em arquivo de registro exige **releitura e conferência de integridade** (numeração contínua, contagem de entradas, nenhuma entrada anterior sobrescrita) antes de reportar sucesso. Uma nota foi acidentalmente sobrescrita por edição sem conferência. Vale para qualquer skill que grave, não só a `analise-desempenho`.

**Restrição operacional assumida:** a cópia em `/mnt/project/` é somente-leitura. O fluxo real é gerar a versão editada em `/mnt/user-data/outputs/` e o aluno **baixar e re-subir** na base do project. A skill deve **avisar isso ao final** — sem o re-upload, o registro se perde.

**Fronteira:** o caderno não reabre a otimização-primeiro. Ele é **derivado do que o aluno errou e perguntou** (pós-tentativa, D13), nunca material antecipado. E a skill guarda o **protocolo**; o caso concreto fica no caderno — é o "elo por tipo, não por cópia" do D11 aplicado à camada de estado.

### D15 — Versionamento embutido e entrega sempre integral

**Contexto:** o sistema já produz artefatos em várias camadas (skills, prompts magros, docs de decisão, cadernos, templates) e passou a receber patches recorrentes. Sem marca de versão, deixa de ser possível saber qual cópia está subida na conta ou na base do project — e a entrega por trecho ("insira isto na seção X") transfere ao aluno o trabalho de montagem, com risco de sobrescrita (já ocorrido: uma nota apagada por edição sem conferência, §5 do handoff das notas).

**Decisão — dois combinados globais, válidos em qualquer chat e qualquer project:**

1. **Todo artefato carrega sua versão embutida**, no lugar apropriado ao formato:
   - **Skill** — linha de versão logo abaixo do H1 + seção final **`## Histórico de versões`** (tabela versão · data · mudança). *Não* no frontmatter: `name` e `description` são os campos que o carregador lê.
   - **Prompt magro de Project-filho** — linha `Versão X.Y · AAAA-MM-DD` no topo do prompt.
   - **Documento de base (decisões, inventário)** — linha de versão sob o título, com o resumo do que mudou desde a anterior.
   - **Arquivo vivo (caderno)** — versiona por **data de atualização + contagem de entradas** no cabeçalho, não por número: ele muda toda sessão, e numerá-lo geraria ruído sem informação.
   - **Artefato derivado (caderno de revisão, material de sessão)** — data e sessão de origem no próprio arquivo.
2. **Numeração:** `MAJOR.MINOR`. **MINOR** = patch de conteúdo, acréscimo de bloco, correção. **MAJOR** = mudança estrutural (seções novas, mudança de escopo ou de fronteira entre camadas).
3. **Entrega sempre integral.** Ao patchar qualquer artefato, entregar a **versão completa já atualizada**, pronta para substituir a anterior — nunca só o trecho novo. Quando o integral for inviável (artefato grande demais, ou edição em arquivo que não está em mãos), o trecho vem com **instrução cirúrgica**: âncora exata de onde entra (texto imediatamente anterior/posterior), o que substitui, e o que conferir depois de inserir. *Exceção revogada pelo **D26** (2026-09-15): não há caso inviável — sem o arquivo íntegro em mãos, pede-se o arquivo.*

**Por quê:** versão embutida transforma "qual está subida?" de arqueologia em leitura de uma linha — e o histórico no próprio arquivo mantém o *porquê* colado ao *quê*, que é o mesmo princípio deste documento. Entrega integral elimina a classe de erro mais cara observada até aqui (montagem manual com sobrescrita) e casa com a restrição operacional do D14: como o fluxo real é **baixar e re-subir**, o artefato tem de chegar pronto para substituir, não para ser costurado.

**Fronteira:** versionar não é gerar changelog cerimonial. O histórico é uma tabela curta de linhas de uma frase; se uma mudança não merece uma frase, não merece bump de versão.

### D16 — Prompt de estado: aponta, não enuncia

**Contexto:** o D3 ("inteligência nas skills, não nos prompts") ganhou o apelido de *prompt magro*, e o apelido passou a ser lido como métrica de tamanho. Com o crescimento da arquitetura (cinco skills por professor, dial do D13, caderno do D14), o prompt do professor de Contabilidade chegou a ~55 linhas e apareceu a dúvida de se o D3 estava sendo violado.

**Diagnóstico:** não estava — mas o D3 estava mal enunciado. O que ele decidiu é *onde mora a inteligência reutilizável*, não *quantas linhas o prompt tem*. Um prompt pode ser longo e obedecer ao D3, desde que o que o alonga seja **estado local**.

**Decisão:**

1. **O nome passa a ser "prompt de estado"** (o termo "prompt magro" fica como sinônimo histórico). O nome descreve o que ele é e para de sugerir que curto é bom em si.
2. **Critério de alocação — teste da portabilidade:** *esta linha faria sentido copiada para o professor de Redes?* Sim → é inteligência → **skill**. Só faz sentido aqui → é estado → **prompt** (dial, bancas-alvo, nome do caderno, escopo dentro/fora, jeito de estudar).
3. **O prompt aponta, nunca enuncia.** Citar a skill e o nome do protocolo é ponteiro; reproduzir a regra em prosa é **eco**. Eco é dívida técnica: no dia em que a skill mudar e o prompt não, o professor obedece a uma versão fantasma. Ponteiro sobrevive a qualquer patch.
4. **Teto operacional, não estético:** prompt acima de ~60 linhas, ou que repita regra de skill em mais de dois pontos, é sinal de vazamento — revisar no passe de promoção (D14).

**Por quê:** o risco real nunca foi volume, foi **deriva por duplicação**. O v2.0 do prompt de Contabilidade tinha três ecos (justificativa do aluno, diagnóstico-como-hipótese, proibição de material pré-mastigado) — todos já escritos por extenso nas skills. Convertidos em ponteiro, o prompt encolheu como *consequência* da regra certa, não como meta.

**Fronteira:** ponteiro não é vago. "Siga a `resolucao-questoes`" sozinho é fraco; "siga o protocolo de input da `resolucao-questoes`" nomeia o gancho e dispara a skill certa. Nomear o protocolo é ponteiro; explicar como ele funciona é eco.

### D17 — O documento de decisões é estável; o backlog é vivo

**Contexto:** este documento foi de v7.0 a v7.1 sem que nenhuma decisão mudasse — o que mudou foram as seções **Estado atual** (inventário de skills e professores) e **Fios soltos** (fila de trabalho). Ou seja: duas seções vivas dentro de um artefato estável, forçando bump de versão do conjunto a cada sessão. É o mesmo defeito que o D14 diagnosticou nas skills de disciplina, agora no Project-mãe.

**Decisão:** aplicar o D14 ao ateliê.

- **Estável — este documento.** Decisões (D1…Dn), princípios invioláveis, glossário. Muda **apenas** quando nasce ou se altera uma decisão.
- **Vivo — `backlog-atelie.md`**, na base do Project-mãe. Três seções: (1) *Estado atual do sistema* — inventário com versões de skills, professores e cadernos; (2) *Fila de trabalho* — itens por criticidade, cada um com o porquê e a dependência; (3) *Fricções registradas* — as notas de melhoria 8 em diante.

O documento de decisões **aponta** para o backlog e não repete seu conteúdo — mesma relação entre a skill de disciplina e o caderno (D14), e mesmo princípio de ponteiro × eco do D16.

**Por quê:** um artefato só é barato de manter se o que muda nele muda por um motivo só. Misturar decisão (rara, argumentativa, definitiva) com inventário (semanal, factual, descartável) obriga a regenerar o todo para atualizar a parte — e faz o histórico de versões perder sentido, porque "v7.1" passa a significar "alguém subiu uma skill", não "o sistema pensa diferente".

**Formato — markdown, não planilha:** poucas linhas heterogêneas, em que o *porquê* de cada item importa mais que qualquer campo, e um fluxo operacional de baixar-e-re-subir. Planilha compensaria com muitas linhas homogêneas, filtro e ordenação; não é o caso.

**Anti-cerimônia (as três travas do backlog):**
1. **Uma linha por item**, com o porquê junto quando ele não for óbvio.
2. **Item concluído sai da fila** — não vira histórico riscado. O registro do que foi feito já mora no histórico de versões do artefato afetado (D15).
3. **Sem status intermediário.** O item está na fila ou não está. "Em andamento" com três semanas de idade é ruído, não informação.

**Efeito colateral desejado:** as notas de melhoria deixam de ser um arquivo próprio. As 7 originais viram histórico fechado (`notas-melhoria-skills.md` 1.1, todas implementadas); as novas nascem na seção 3 do backlog. Um artefato vivo no ateliê em vez de dois.

**Fronteira:** o backlog não guarda decisão. Se um item da fila exigir escolha argumentada ("vale uma skill própria ou um bloco?"), a escolha vira D aqui — e o backlog fica com a tarefa, apontando para o D.

### D18 — O sistema precisa de um mapa, não de um orquestrador

**Contexto:** o conjunto (Project-mãe, seis Projects-filhos, dez skills, quatro tipos de artefato, dezessete decisões) cresceu a ponto de não caber mais na cabeça. O sintoma relatado foi dificuldade de "enxergar a arquitetura, orquestrar, ver o fluxo e o funcionamento como um todo", com a hipótese de estruturar tudo num repositório GitLab.

**Diagnóstico:** o desconforto é de **legibilidade**, não de coordenação nem de versionamento. A coordenação já existe e funciona sem maestro — skills disparam por relevância, o prompt de estado declara o local, o caderno acumula, o passe promove. O versionamento já existe embutido (D15). O que falta é um artefato que descreva o **conjunto**: hoje a informação está fragmentada entre o doc de decisões (o *porquê*), o backlog (o *estado*) e as skills (o *como* de cada peça), sem nenhum que mostre o todo.

**Decisão:** criar um **`mapa-do-sistema.md`**, estável, na base do Project-mãe, de uma página, com quatro conteúdos: (1) as camadas (conta / project / arquivo local e por quê); (2) o ciclo de vida de um registro (questão errada → diagnóstico → caderno → consolidação → promoção → skill); (3) a tabela "quem escreve o quê / onde isso mora"; (4) as rotinas (sessão de estudo, sessão de ateliê, passe de promoção). Acompanha um **diagrama** no Design System da `recursos-visuais` — três camadas, dois tipos de project, setas de quem alimenta quem.

É **artefato estável** (muda quando muda uma decisão), então mora junto deste documento, não do backlog. A tarefa de produzi-lo é o item B2 do backlog, dependente do test-drive (B1): o teste pode alterar o fluxo que o mapa vai desenhar.

**Contra o GitLab, por ora:** Git resolveria backup externo e diff, mas nenhum dos dois é o problema atual, e introduziria uma **terceira cópia** do sistema (instalada, `outputs`, repositório) — reabrindo a ambiguidade de "qual é a verdadeira" que o D15 fechou. Só passa a valer se o repositório for declarado **fonte da verdade** e subir na conta virar *deploy*, não edição; e, mesmo assim, repositório burro (pastas + README-mapa, sem CI, sem automação, sem gestão de tarefas — o backlog continua onde se trabalha). Reavaliar depois de um ciclo, se persistir a falta de backup externo. *Gatilho acionado pelo **D27** (2026-09-16): o Git entra como histórico e backup, não como fonte da verdade — as duas objeções deste parágrafo ficam de pé.*

**Fronteira — anti-over-engineering:** a régua a partir daqui é que **cada melhoria de arquitetura se pague em sessões de estudo melhores**. Enquanto o sistema estava sendo construído, a proporção se justificava; agora não. Se uma semana passar sem resolução de questões, o sistema virou o hobby — e o objetivo é o concurso, não a elegância da arquitetura. O mapa entra porque *reduz* carga (legibilidade), não porque adiciona estrutura.

**Escopo deixado de fora, deliberadamente:** as *convenções pessoais de trabalho com IA* (versionamento, ADR, handoff, prompt de estado, quando criar skill × project) são transversais a todos os domínios do usuário — trabalho, estudos, outros — e não pertencem a este ateliê. Colocá-las aqui seria o eco do D16 em escala maior. Ficam registradas em handoff próprio, para discussão fora deste project.

### D19 — Código não viaja nu

**Contexto:** o material de revisão gerado no test-drive (`revisao-sessao-2026-07-23.html`) glosava espontaneamente os códigos da própria sessão — *"contrato a executar (E14)"*, *"leitura 'em X' (E13)"* — mas deixava **nus** os que apontavam para fora dela: *"reincidência do E12"*, *"foi o erro do E9"*. Dentro do artefato o leitor tinha acabado de ver o caso; fora dele, o código é opaco. Semanas depois, que é exatamente quando o material de revisão se lê, as duas metades do mesmo arquivo têm legibilidades opostas.

**Decisão:** em texto voltado ao aluno, **a glosa vem primeiro e o código entre parênteses** — *máscara de coincidência de data (E14)*, *inversão de mecanismo (P4)*. Nunca o inverso, nunca nu.

**Fronteira (obrigatório × dispensável):**

- **Obrigatório** quando o código aponta para **fora do artefato corrente**, ou quando é usado como **argumento** ("reincidência de X", "mesmo mecanismo de Y").
- **Dispensável** quando o próprio artefato acabou de descrever o caso; **dentro de catálogo ou coluna com legenda à vista** (as listas P1–P6 da skill, a coluna "Padrão" do caderno); e em **enumeração-índice** ("a lacuna acumula E4, E5, E9…"), em que quem nomeia o mecanismo é a frase que envolve os códigos.

**Por quê:** é a regra 9 de `recursos-visuais` — autocontenção de contexto — aplicada ao **texto**. O que a motivou lá vale aqui sem alteração: um artefato de revisão só cumpre a função se fizer sentido lido sozinho, fora do chat que o gerou. Código nu transfere ao aluno o custo de arqueologia justamente no momento em que ele tem menos contexto.

**Alocação (elo por tipo, não cópia — D11):** cada skill enuncia a regra para o **seu** catálogo. `resolucao-questoes` para P1–P6 e Famílias; `analise-desempenho` para E# e para o schema do caderno. Nenhuma enuncia a do outro.

**Fronteira anti-cerimônia:** não é gerar changelog nem reescrever em massa os catálogos existentes. É convenção de escrita para artefato novo e para o que for tocado daqui para frente.

### D20 — O visual tem dois públicos

**Contexto:** no test-drive de Desenvolvimento de Software, a nota do professor sobre "repertório de técnicas manuais" (tabela de rastreio, grade de vetor com índices, pilha de chamadas recursivas) chegou a propor skill transversal nova. O instrumento em si é conteúdo de disciplina e já tem casa pelo D14, que lista "instrumentos de rascunho" como artefato estável de skill de disciplina; skill nova não se pagaria (D18). Mas a nota descobriu, sem nomear, outra coisa: nem todo visual que o professor gera tem o mesmo destinatário.

**Decisão:** distinguir dois tipos de visual.

- **Visual de ancoragem** — o professor produz, o aluno **lê**. Design System livre: pergaminho, cor, HTML/SVG, layout amplo. Fixa o mecanismo depois da tentativa (D13).
- **Visual-instrumento** — o professor ensina, o aluno **redesenha à mão**, na folha de rascunho, sob pressão de prova. Restrição de projeto: cabe em **A4**, **cor nunca carrega informação**, sem dependência de layout ou software, reproduzível a lápis em poucos traços.

Técnica que só funciona colorida ou renderizada **é ilustração de ancoragem, não instrumento** — e deve ser apresentada como tal.

**Por quê:** o instrumento existe para ser usado onde não há cor, tela nem layout. Ensinar instrumento que o aluno não consegue redesenhar é a ilusão de fluência do D1 na sua versão visual: ele reconhece o traço quando vê e não sabe produzi-lo quando precisa. A distinção também explica por que a nota parecia pedir skill nova — o *instrumento* é de disciplina (varia com o método: traço de execução em Lógica, razonete em Contabilidade, esquema de camadas em Redes), mas a *restrição de projeto* é transversal.

**Alocação (elo por tipo, não cópia — D11):** `recursos-visuais` enuncia a distinção e a restrição; cada skill de disciplina traz o seu catálogo de instrumentos.

**Fronteira:** não rebaixa o visual de ancoragem nem impõe austeridade geral — "abundância, não parcimônia" (D13) segue valendo para ancoragem. A restrição incide só sobre o que é apresentado como instrumento reproduzível.

**Mecanismo:** `recursos-visuais` 1.2 (seção "Dois públicos: ancorar × instrumentar", com a instrução de ensinar o traço e não só o resultado; quatro formas novas no catálogo marcadas como instrumento); `analise-desempenho` 1.2 (na curadoria do material derivado, instrumento vence ilustração em caso de empate).

### D21 — Fonte primária da apostila; PDF como fallback aceito; teto da base do Project-filho

**Contexto:** cursos costumam oferecer material "original" e "reduzido" — versão mais curta, também produzida pelo próprio curso (não é reescrita de terceiro, mas corta conteúdo). A ingestão de apostila (item B5 do backlog) converte PDF em `.md` para caber na janela de contexto e melhorar a recuperação, mas a conversão é trabalho semi-automático e pode não acontecer a tempo de todas as disciplinas antes de a matéria entrar em estudo — bloquear o estudo por falta de conversão contraria o D18.

**Decisão:** a fonte primária de conversão é sempre o material **original** — nunca o reduzido, porque o reduzido corta conteúdo que pode cair em prova. Slides ficam fora do pipeline de texto por padrão, reservados a uso pontual como visual-instrumento (D20). A base do Project-filho aceita tanto **`.md` convertido** quanto **PDF bruto como fallback**, para os casos em que não houve tempo de converter — mas `.md` é sempre preferível: PDF bruto consome mais token pela mesma informação (a razão de ser do B5) e degrada a recuperação quando o conhecimento excede a janela de contexto. Fallback é situação temporária, não segunda via permanente: sinalizar no prompt de estado ou no caderno quais fontes ainda estão em PDF bruto, para priorizar a reconversão.

**Por quê:** sustenta D6 (hierarquia de fontes) e D8 (fidelidade) na escolha do material; equilibra isso com a realidade operacional de que a conversão nem sempre acompanha o ritmo de estudo.

**Fronteira:** não decide qual conversor usar por disciplina — mecânica de ferramenta, resolvida à parte (PyMuPDF4LLM como padrão; Docling ou Marker onde tabela e fórmula carregam a informação).

### D22 — Pasta local sincronizada é a fonte da verdade fria ~~(vigente)~~ · **REVOGADA pelo D23 em 2026-08-11**

> **Status: revogada.** O registro fica aqui por inteiro — decisão revogada não se apaga, se anota (mesmo princípio do D15: o *porquê* colado ao *quê*, inclusive quando o quê muda de novo). O que segue é o texto original, válido apenas como histórico; a regra vigente está no **D23**.

**Contexto:** o D18 recusou o GitLab "por ora", mas deixou o próprio gatilho de reabertura escrito: reavaliar se persistir a falta de backup externo. O ciclo passou, e persiste. O D18 também deixou em aberto, sem resolver, o lugar de um plugin de produtividade (`TASKS.md`) para gestão de tarefas do dia a dia — ponto retomado aqui.

**Decisão:** cria-se `06-sistema-professores`, pasta irmã das já existentes em `H:\Meu Drive\riclimavieira\concursos` (sincronizada via Google Drive), como **fonte da verdade fria** — onde o artefato é editado e existe entre sessões. A cópia instalada (skill na conta, arquivo na base do Project-filho) é **cópia em execução**: subir é *deploy*, não edição; divergiu, a pasta local ganha. `/mnt/user-data/outputs/` nunca é fonte, só correia de transmissão. Layout: `atelie/` (decisões, backlog, template, mapa), `skills/` (uma subpasta por skill — prefixo `skill-` só no **nome da pasta local**, não altera o campo `name` da skill instalada na conta, não dispara repontero de prompt nenhum, D15/D16 preservados), `professores/<disciplina>/{prompt-estado.md, caderno, apostila/}`, `ferramentas/{ingestao-apostila/, planilha/}`. Sem pasta própria de metas (aponta para `03-mentorias/lsconcursos/metas`, já existente) nem de planilha de controle (fica em `01-gestao-e-editais`, é dado — só a ferramenta `parse_meta.py` entra em `ferramentas/planilha/`).

**Plugin de Produtividade — resolvido dentro desta decisão:** cobre só a camada operacional (rodar o conversor, prazos da LS, lembretes do dia a dia). A fila de arquitetura do sistema continua exclusivamente na seção 2 do `backlog-atelie.md` — sem emenda ao D17, sem segundo artefato vivo concorrente.

**Por quê:** resolve backup externo e cópia de trabalho sem reabrir a ambiguidade de "qual é a verdadeira" que motivou a recusa ao Git — aqui há só duas cópias, com hierarquia clara, nunca três.

**Fronteira:** sem CI, sem automação, sem gestão de tarefas de arquitetura pelo plugin — a fila de trabalho do sistema continua no backlog.

### D23 — Reversão do D22: duas cópias, sem camada de pasta local

**Contexto:** o D22 foi ratificado no mesmo dia em que se descobriu o que ele pressupunha sem dizer. A pasta local como *fonte fria* só entrega o que promete se o assistente puder ler e escrever nela diretamente — o que, na prática, exige rodar o ateliê no Cowork do app Desktop com a pasta conectada. Ao examinar essa migração, três coisas apareceram: (a) mesmo em Cowork, o *deploy* continua manual, porque a sessão não escreve na base de conhecimento de um Project — some o passo de baixar, não o de subir; (b) a raiz é um drive mapeado do Google Drive (`H:\`), e drive mapeado pode não ser alcançável por comando de shell, justamente o que o B5 e o empacotamento de skill precisam; (c) o ateliê e todos os Projects-filhos vão continuar rodando em **chat web**, por decisão de uso.

**Decisão:** revoga-se o D22. Volta a valer o modelo de **duas cópias**, que é o que o D10 e o D15 já descreviam:

- **Cópia em execução** — skill na conta, arquivo na base do Project (mãe ou filho). É onde o artefato vive e é lido.
- **Correia de transmissão** — `/mnt/user-data/outputs/`: onde a versão nova é gerada, para o arquiteto **baixar e re-subir** (D14/D15). Nunca é fonte, e agora também não há terceira camada acima dela. *Emendado pelo **D28** (2026-09-16): onde a sessão escrever na base, a entrega termina lá e o re-upload cai.*

Não existe mais "fonte da verdade fria" nem hierarquia de desempate entre cópias: divergência não é resolvida por regra de precedência, e sim pela entrega integral do D15 — o artefato chega pronto para substituir o anterior, o que torna a divergência um evento e não um estado.

**Backup do sistema fora do claude.ai continua sem solução declarada.** O gatilho escrito no D18 (reavaliar se persistir a falta de backup externo) segue **aberto** — o D22 tinha sido a resposta a ele, e a resposta caiu. Cópia manual da pasta para o Drive continua possível como hábito pessoal; o que deixa de existir é o *contrato* de que aquela cópia manda. *Gatilho fechado pelo **D27** (2026-09-16).*

**Plugin de Produtividade — volta a ficar em aberto.** O D22 o havia resolvido "dentro de si"; revogado o D22, o item volta à fila (M7) sem destino definido. Registro do que se apurou, para não refazer a análise: o plugin é um conjunto de arquivos (`TASKS.md`, `dashboard.html`, `CLAUDE.md`, `memory/`) que vive no diretório de trabalho — em chat web esse diretório é efêmero, então o painel visual, o auto-save e a observação de mudança externa **não funcionam**; sobra um markdown de tarefas comum. O escopo, se um dia entrar, continua sendo o que o D22 delimitou e esta revogação preserva: **camada operacional apenas** (prazos, lembretes, rodar ferramenta) — a fila de arquitetura do sistema é exclusiva do `backlog-atelie.md`, sem segundo artefato vivo concorrente (D17).

**Por quê:** o D18 fixou a régua de que cada peça de arquitetura tem de se pagar em sessões de estudo melhores. O D22 cobrava um custo real — migrar de superfície, aprender outro modo de trabalho, manter uma terceira localização em dia — contra um benefício que, no uso declarado (chat web), não se realiza. Reverter é a régua do D18 funcionando, não um recuo.

**Fronteira:** o D21 **não** é afetado — a regra de fonte da apostila (original nunca reduzido; PDF bruto como fallback temporário) independe de onde o arquivo mora. O que cai é só a camada de armazenamento e a hierarquia entre cópias.

### D24 — Artefato vivo por natureza de uso; o Project-filho sustenta três (emenda ao D14)

**Contexto:** o D14 decidiu **um único** arquivo vivo por Project-filho, com justificativa explícita: a fricção de baixar-e-re-subir a cada sessão é o que faz protocolo ser abandonado na prática. O campo desmentiu a premissa em duas frentes ao mesmo tempo. O Project de Engenharia de Software atravessou a tarefa 10 inteira (30+ questões) com **três** arquivos vivos — caderno, CSV de cartões e notas de melhoria — sem abandono de nenhum. E o mecanismo de memorização, que não existia em skill nem em template, nasceu sozinho em **duas rotas incompatíveis**: seção 1.4 em tabela markdown dentro do caderno de Tributário (C1–C8) e arquivo CSV irmão em Engenharia de Software (35 cartões). Duas implementações da mesma necessidade divergindo em *lugar*, não só em schema, é dívida que encarece a cada sessão.

**Decisão:** o critério de alocação deixa de ser *quantidade* e passa a ser **natureza de uso**. Cada Project-filho sustenta até **três** artefatos vivos, em **lista fechada**:

1. **`caderno-<disciplina>.md`** — *registro*. Estado do aluno, dossiê de banca, errata da fonte (D14). Formato definido pelo sistema.
2. **`flashcards-<disciplina>.csv`** — *memorização*. Formato definido por **ferramenta externa** (Anki), não pelo sistema.
3. **`notas-de-melhoria-<disciplina>.md`** — *fricção*. O que o professor ou o método falharam em entregar, observado na própria sessão de estudo. É a matéria-prima de onde nascem os itens do ateliê.

**Por que o cartão não cabe dentro do caderno:** seu formato é ditado de fora — colunas fixas, separador declarado, cabeçalhos `#chave:valor`, HTML nos campos. Embutir isso em tabela markdown obriga a uma conversão manual a cada importação, e conversão manual recorrente é exatamente o que o D14 nomeia como causa de protocolo abandonado. O mesmo argumento do D14 aponta, aqui, para o lado oposto.

**Por que a fricção não sobe direto ao backlog:** o backlog é do Project-mãe e se atualiza em **sessão de ateliê**. A fricção nasce em **sessão de estudo**, quando o arquiteto está de chapéu de aluno. Exigir que ele abra o ateliê no meio do estudo para registrá-la contraria o D18 (estudo antes de ateliê) — e o que não se registra na hora se perde, que é a premissa de todo este protocolo.

**A trava que preserva o D14 — fila de saída, não acervo:** as notas de melhoria **esvaziam** no fechamento da tarefa. Triadas para a seção 3 do backlog em sessão de ateliê, são **podadas do arquivo**. O caderno e o CSV acumulam, cada um com as suas travas próprias (consolidação e poda no caderno, D14; critério de admissão do cartão, abaixo); o arquivo de notas, não. Arquivo vivo que só cresce e nunca esvazia é o que o D14 temia, e é isso que fica proibido — não a existência do terceiro arquivo.

**Critério de admissão do cartão (a trava do CSV):** vira cartão apenas o **conteúdo arbitrário** — lista fechada, par que se troca, rótulo, número, dispositivo, definição literal cobrada. Onde há **critério gerador** (a resposta se deduz), não se emite cartão: o remédio é compreensão, e o destino é o material derivado de revisão. É a bifurcação da `metodo-professor` 1.2 aplicada à emissão. Isto substitui qualquer teto numérico por sessão: o que infla o baralho é cartão de coisa dedutível, não volume de cartão legítimo.

**Fronteira:** três, nomeados, lista fechada. Um quarto artefato vivo exige emenda a esta decisão, não conveniência de sessão. O que não couber nos três ou é registro (vai ao caderno) ou é ateliê (vai ao backlog).

**Emenda ao D14:** onde o D14 diz *um único arquivo por Project-filho*, leia-se *um único arquivo por natureza de uso, entre as três nomeadas aqui*. O princípio do D14 — **minimizar artefatos vivos, não artefatos totais** — segue intacto: o que ele mede é carga operacional simultânea, e as três naturezas não competem entre si dentro de uma sessão.

### D25 — O Project existe por disciplina; o caderno tem dois eixos de indicador

**Contexto:** três itens do backlog vinham aplicando, por precedente, uma regra que nunca foi decidida: o **L6** adiou o Project de Legislação Tributária Estadual porque a tarefa era leitura pura, o **C7** adiou Português pelo mesmo motivo, e o **C4** registrou Governança de TI como "teoria — sem gatilho". O critério de abertura tinha virado *ter bateria de questões*. Na sessão de 2026-09-11, ao abrir o professor de Governança de TI, o arquiteto nomeou o que o precedente estava custando: o Project-filho não é só a casa da bateria — é o **repositório das perguntas e dúvidas** dele, de conteúdo e de questão. Sem Project aberto, a dúvida de teoria acontece em chat comum e evapora com a aba.

**Decisão, em duas partes:**

1. **O Project-filho abre com a disciplina, não com a bateria.** Toda disciplina em estudo tem Project, prompt de estado e caderno instanciado, haja ou não questões. O que a ausência de bateria adia é a **skill de disciplina** — essa continua dependendo de questão real, porque catálogo de pegadinha sem campo é invenção (D8). Abrir Project é barato; inventar catálogo é caro.
2. **O caderno passa a registrar dois eixos**, com indicador próprio cada:
   - **Eixo conteúdo** — bloco 1.1, entradas **T#** (travamentos). Nasce da leitura: onde travei, em que aula/página, com que **carga** (intrínseca × extrínseca, D2), o que destravou, se reincidiu. Indicador: **densidade** de travamento por volume lido, **carga dominante** por tema e reincidência.
   - **Eixo questão** — bloco 1.2, entradas **E#**, como já existia. Indicador: placar de três parcelas e padrão dominante.

**Por quê (parte 1):** o gatilho por bateria confundia *o que o Project serve* com *o que o Project mede*. Ele serve para acumular a interação — pergunta, dúvida, explicação, registro — e isso começa na primeira leitura. Medir só quando há questão é o que torna a disciplina de teoria invisível no sistema, exatamente onde a evasão de dúvida é maior, porque não há gabarito para denunciá-la.

**Por quê (parte 2):** os dois eixos medem habilidades diferentes e um não prevê o outro — dá para entender bem e errar na prova (falha de técnica), e dá para acertar por reconhecimento sem ter entendido (a ilusão de fluência do D1, agora visível no cruzamento). O cruzamento é o produto novo: erro de conteúdo num tema com travamento registrado é **dúvida adiada, não fechada** — e isso nenhuma das duas tabelas mostra sozinha.

**A carga como indicador de quem tem o problema:** a coluna intrínseca × extrínseca transforma o D2, que era um critério de decisão do professor no momento de explicar, em **série histórica**. Extrínseca dominante num tema deixa de ser impressão e vira evidência sobre a **fonte** — com destino declarado: errata (Seção 3) ou troca de material, nunca "estudar mais". É também a fronteira que este D fixa: **carga extrínseca não é errata** — a fonte mal escrita não é fonte errada.

**As travas que impedem o caderno de virar diário (o D14 preservado):**

1. **Critério de admissão do T#:** só entra o que o aluno **não teria resolvido sozinho relendo o trecho**. Curiosidade lateral, checagem e pedido de exemplo sobre ponto já entendido ficam de fora. É o espelho do "não registre acerto limpo".
2. **Consolidação por reincidência:** três travamentos no mesmo ponto viram **lacuna estrutural** (bloco 1.3) e os T# que a formaram são podados, guardando origem e data — poda reversível, mesma razão da regra consolidada do dossiê. A 1.1 cresce com **pontos distintos que o aluno não decodifica sozinho**, conjunto pequeno, não com o número de perguntas feitas.

**Fronteira — o que o D25 não faz:** não reabre a otimização-primeiro. O T# é registro **pós-travamento**, derivado do que já aconteceu; continua proibido varrer o capítulo em busca de dificuldades futuras (o M13 do backlog, que discute triagem preventiva, segue pendente e não é resolvido aqui). Não cria artefato vivo novo — os três do D24 seguem sendo três, e o eixo novo mora dentro do caderno. E não altera as travas do D14: schema de uma linha no dossiê, consolidação e promoção em passe deliberado seguem idênticos.

**Mecanismo:** template do caderno **1.3 → 2.0** (bloco 1.1 novo, renumeração de 1.2/1.3/1.4, tipo de sessão, carimbo e controle de integridade com T#); `analise-desempenho` **2.1 → 2.2** (gatilho de registro sem questão, schema T#, cruzamento entre eixos, trava de consolidação do eixo conteúdo, fechamento com placar de teoria, regras inegociáveis 16 e 17); backlog (L6, C7 e C4 perdem a condição de gatilho por bateria).

### D26 — Arquivo de edições é método, nunca entregável (emenda ao D15)

**Contexto:** o item 3 do D15 decidiu a entrega sempre integral, mas deixou uma porta: *"quando o integral for inviável (artefato grande demais, ou edição em arquivo que não está em mãos), o trecho vem com instrução cirúrgica"*. Em 2026-09-11 as duas entregas de ateliê do dia saíram por essa porta, com a mesma justificativa — *grande demais*: `backlog-edicoes-1_29.md` e `D25-insercao-doc-decisoes-8_7.md`. As duas foram salvas na base **no lugar** dos documentos íntegros, e as versões completas anteriores saíram dela. Custo medido, não estimado: o backlog 1.28 sumiu da base e a 1.29 nunca foi aplicada; o documento de decisões ficou sem nenhuma cópia íntegra na base por quatro dias; uma sessão de estudo escolheu tarefa lendo o backlog 1.26, com um bloqueio que já tinha caído; uma sessão de ateliê (2026-09-15) parou sem conseguir inserir notas; e a reconstituição (backlog 1.30, decisões 8.7) exigiu recuperar texto literal de conversas antigas. A justificativa não se sustentava: os dois documentos, com 69 KB e 56 KB, saíram integrais na reconstituição sem nenhuma dificuldade.

**Decisão:**

1. **Edições são método interno de trabalho, nunca entregável.** Todo patch de artefato textual versionado segue o fluxo *gerar as edições → aplicar sobre a cópia íntegra → verificar → entregar só o integral*. A aplicação é mecânica, feita pelo script da skill operacional **`entrega-de-artefato`**: âncora com casamento único, e nada é gravado se uma âncora falhar.
2. **As duas exceções do item 3 do D15 caem.** *Grande demais* deixa de ser caso: o script aplica as edições sobre o arquivo, então o tamanho do artefato nunca passa pela redação. *Arquivo que não está em mãos* passa a significar **pedir o arquivo** — nunca emitir trecho, nunca reconstruir de memória (fricção 8).
3. **O nome é trava.** Nome com *edicoes*, *insercao*, *patch* ou *delta* não sai para outputs. *Emendado pelo **D27** (2026-09-16): o arquivo entregue carrega só o nome do artefato, fixo e sem versão; a versão aparece dentro dele.*
4. **Checagem de quem sobe.** Antes de subir arquivo na base: a primeira linha é o título do artefato, e a versão declarada dentro dele é a que se acabou de gerar. Se não for, não sobe. *Emendado pelo **D27** (2026-09-16): a conferência era contra a versão do nome, que deixou de existir.*

**Por quê:** o D15 já tinha identificado a classe de erro mais cara — montagem manual com sobrescrita — e a exceção era a porta por onde ela voltava, agora pior: o arquivo de edições *parece* o documento, então o erro deixa de ser uma montagem malfeita e passa a ser a substituição do documento inteiro por um fragmento dele. E o registro sozinho não segura: o D15 existia, estava na base e foi lido — e a exceção foi usada mesmo assim. Regra que precisa disparar **no momento da entrega** mora em skill com script, não em documento (D3), pela mesma razão que a entrega de `SKILL.md` mora na `empacotamento-de-skill`. O script também fecha a lacuna da fricção 18: protocolo de âncora para artefato do ateliê, que até aqui só existia para o caderno.

**Fronteira:** não altera os itens 1 e 2 do D15 (versão embutida, numeração). Não cobre `SKILL.md`, que segue na `empacotamento-de-skill` — com a mesma exceção retirada dela — nem caderno e CSV de cartões, cuja escrita é da `analise-desempenho` e já sai integral. Não proíbe mostrar ao arquiteto o que mudou: o resumo do que mudou e por quê continua obrigatório **na resposta**; o que sai de circulação é o arquivo de edições como coisa entregue. O script garante mecânica — âncora, versão, tabela —, não semântica: contagens e referências cruzadas continuam em conferência manual.

**Mecanismo:** skill `entrega-de-artefato` **1.0** (script `aplicar_edicoes.py`, validado reconstruindo esta própria série — a 8.7 saiu byte a byte igual à da base); `empacotamento-de-skill` **1.3 → 1.4** (retira a exceção do integral inviável); uma linha de ponteiro nas instruções do Project-mãe (D16); no backlog, fricção 18 fechada e o incidente registrado como fricção fechada.

**Emenda ao D15:** onde o item 3 diz *"quando o integral for inviável… o trecho vem com instrução cirúrgica"*, leia-se: não há caso inviável; sem o arquivo íntegro em mãos, pede-se o arquivo.

### D27 — Repositório Git como histórico e backup externo; nome fixo (emenda ao D18, ao D23 e ao D26)

**Contexto:** em 2026-09-16 foi preciso recuperar o backlog e o documento de decisões, e as versões anteriores não estavam em lugar nenhum. A base do Project guarda só o que está subido, e o nome com versão (`-v8_8.md`) faz de cada versão um **arquivo novo**: o anterior só sai de cena quando alguém o retira à mão, e retirado, some. O histórico de versões do Google Drive não cobre o caso — ele registra sobrescrita do *mesmo* arquivo, e ainda assim expira em 30 dias ou 100 revisões, salvo marcação manual de "Manter para sempre". O D18 recusou o Git "por ora" e deixou o gatilho de reabertura escrito (reavaliar se persistir a falta de backup externo); o D22 foi a resposta a esse gatilho, o D23 a revogou e registrou o gatilho como **aberto**. Um ciclo depois, a falta cobrou o preço previsto.

**Decisão:**

1. **Repositório Git privado, único para o sistema inteiro** — local em `D:\dev\pessoal\sistema-professores` (disco local não sincronizado, confirmado pelo arquiteto), espelhado em repositório privado no GitHub. **Um repositório só**, nunca um por Project-filho: guarda o ateliê inteiro (`atelie/`), as skills (`skills/`) e todos os professores (`professores/<disciplina>/`) sob a mesma raiz. Um repositório por professor multiplicaria o mesmo overhead de manutenção que o D18 recusou pagar por skill de disciplina — a régua não muda por trocar de artefato.
2. **O repositório não é fonte da verdade.** É **histórico e backup**. A cópia em execução (skill na conta, arquivo na base do Project) continua sendo onde o artefato vive e é lido, como o D23 fixou. O commit registra o que foi entregue; não é um terceiro lugar a manter em dia.
3. **Repositório burro**, como o próprio D18 condicionou: pastas e arquivos, sem CI, sem automação, sem gestão de tarefas. A fila de trabalho continua exclusivamente no `backlog-atelie.md` (D17).
4. **Fora do drive sincronizado.** O repositório não mora em `H:\Meu Drive`: a sincronização do Google Drive mexe na pasta `.git` durante a operação do Git e pode corrompê-la. Quem faz o papel de backup externo é o espelho remoto.
5. **Nome fixo, versão só dentro.** Arquivo em minúsculas, hífen entre palavras, sem acento e **sem versão no nome** (`decisoes-de-design.md`, `backlog-atelie.md`). A versão aparece na linha de versão do documento (D15), na mensagem do commit e na tag — sempre com **ponto** (`8.9`), nunca underline. O underline existia só para não pôr ponto dentro de nome de arquivo; sem versão no nome, o motivo desapareceu. **O caminho no repositório espelha o caminho na base** — `atelie/decisoes-de-design.md` é o mesmo caminho relativo nos dois lugares, `professores/<disciplina>/caderno-<disciplina>.md` idem — para o `git diff` ser comparável direto contra o que está subido, sem tradução de lugar.
6. **O diff antes do commit é verificação obrigatória**, não conferência opcional. É o passo que teria denunciado o incidente de 2026-09-11 antes de ele chegar à base: arquivo de edições salvo no lugar do documento aparece no `git diff` como centenas de linhas apagadas.

**Por quê:** o D18 recusou o Git porque o problema de então era **legibilidade**, não versionamento nem backup — e porque um repositório declarado fonte da verdade criaria uma terceira cópia, reabrindo a ambiguidade de "qual é a verdadeira". As duas objeções continuam de pé, e é exatamente isso que os itens 2 e 3 preservam: o repositório entra **abaixo** da cópia em execução, como registro, não acima dela, como fonte. O que mudou foi o problema — não é mais legibilidade, é perda medida de versão anterior, com recuperação por arqueologia de conversa. E o nome fixo ataca a mesma classe de erro do D26 pelo outro lado: com versão no nome, a versão nova é um arquivo *diferente* e alguém precisa retirar o antigo à mão; com nome fixo, ela cai **sobre** o anterior, e o momento em que dois arquivos parecidos convivem na base deixa de existir.

**Fronteira — a régua do D18 continua valendo:** isto se paga porque uma perda já aconteceu e custou uma sessão de recuperação, não porque repositório é elegante. Nada de CI, hooks, submódulos, branches de feature ou gestão de tarefas no Git. Um `commit` e um `push` por entrega; se o fluxo crescer além disso, virou hobby.

**Emenda ao D26:** onde o item 3 diz que o arquivo entregue *"carrega o nome do artefato e a versão (`<artefato>-vX_Y.md`)"*, leia-se: carrega **só o nome do artefato**, fixo, e a versão aparece **dentro** dele. A outra metade do item 3 segue intacta — nome com *edicoes*, *insercao*, *patch* ou *delta* não sai. E onde o item 4 manda conferir se *"a versão bate com a do nome"*, leia-se: conferir se a versão declarada no documento é a que se acabou de gerar.

**Mecanismo:** skill `entrega-de-artefato` **1.0 → 1.1** (comando de saída passa a usar `--versao X.Y`; linha da tabela de travas e fecho obrigatório reescritos para nome fixo). O script `aplicar_edicoes.py` **não muda** — a trava 3 já aceitava `--versao` como alternativa à versão no nome. Renomeação dos artefatos na base e no repositório; no backlog, o item de renomeação e a fricção do incidente de recuperação.

### D28 — A sessão escreve na base do Project; cai o re-upload (emenda ao D23 e ao D14)

**Contexto:** o D14 registrou como **restrição operacional assumida** que a cópia em `/mnt/project/` é somente-leitura e que o fluxo real é o arquiteto **baixar e re-subir**. O D23 foi além e usou a mesma premissa como argumento para revogar o D22: *"mesmo em Cowork, o deploy continua manual, porque a sessão não escreve na base de conhecimento de um Project — some o passo de baixar, não o de subir"*. Em 2026-09-16 a premissa foi testada e é falsa nesta superfície. O teste foi explícito: gravação, segunda gravação no mesmo caminho, leitura de conferência e listagem da base. O documento foi **substituído no lugar**, sem duplicata.

**Decisão:** onde a sessão dispuser da ferramenta de escrita na base, a entrega termina **na base**, não em `outputs`. O passo de re-upload desaparece; o de baixar permanece, porque o arquivo ainda precisa entrar no repositório do D27.

**A trava — conferência pós-escrita, herdada do D14:** gravar não encerra a entrega. Depois de escrever, **ler de volta da base** e conferir três coisas: a primeira linha é o título do artefato, a versão declarada é a nova, e a listagem da base mostra **um** documento naquele caminho. Sem essa leitura, a escrita direta é pior que o re-upload manual, porque tira o arquiteto do circuito sem pôr nada no lugar.

**Fronteira:**

- **Só a base de Project.** Skill continua subindo na conta à mão (D10), e o empacotamento segue na `empacotamento-de-skill`.
- **Só onde a ferramenta existe.** Esta sessão a tem; **o chat web, onde rodam o ateliê e todos os Projects-filhos (D23), ainda não foi verificado**. Enquanto não for, baixar-e-re-subir continua sendo o padrão dos Projects-filhos e o protocolo do caderno (D14) não muda. Verificar é item de backlog, não suposição.
- **Não reabre o D22.** Não há pasta local como fonte fria nem hierarquia de desempate entre cópias. O que muda é só quem executa o último passo.

**Emenda ao D23:** onde o item (a) do Contexto diz que *"a sessão não escreve na base de conhecimento de um Project"*, leia-se: não escrevia na superfície examinada em 2026-08-11; escreve nesta. O resto do D23 fica de pé — inclusive a revogação do D22, que se sustentava também nos itens (b) e (c).

**Emenda ao D14:** onde a *restrição operacional assumida* manda gerar em `outputs` para o arquiteto baixar e re-subir, leia-se: re-subir só onde a sessão não escrever na base.

## Glossário
 
- **Ilusão de fluência:** sentir que aprendeu porque o texto era fácil de ler, sem reter de fato.
- **Trava:** o conjunto de regras que mantém o método como andaime (não reescrita).
- **Carga intrínseca / extrínseca:** dificuldade do assunto / dificuldade imposta pela forma do texto.
- **Prompt de estado** (ex-"prompt magro"): instrução do Project-filho que declara o que é local (dial, bancas, caderno, escopo) e **aponta** para as skills em vez de reproduzir o que elas dizem.
- **Ponteiro × eco:** citar a skill e o nome do protocolo × reproduzir a regra em prosa no prompt (dívida técnica, deriva garantida).
- **Project-mãe / Projects-filhos:** o ateliê das skills e prompts / os professores onde se estuda.
- **Mineração de sinais:** garimpar os marcadores de incidência/pegadinha que o autor já deixou na fonte.
- **Artefato estável × artefato vivo:** o que se edita raramente e em lote (skills) × o que cresce a cada sessão (caderno do project).
- **As três naturezas de artefato vivo do Project-filho (D24):** *registro* (`caderno-<disciplina>.md`) · *memorização* (`flashcards-<disciplina>.csv`) · *fricção* (`notas-de-melhoria-<disciplina>.md`). Lista fechada.
- **Fila de saída × acervo:** arquivo vivo que **esvazia** ao ser triado (as notas de melhoria, podadas no fechamento da tarefa) × arquivo vivo que acumula sob travas próprias (caderno e CSV). O que o D14 proíbe é acervo sem trava, não o terceiro arquivo (D24).
- **Conteúdo arbitrário × critério gerador:** o que só se sabe por memória (lista fechada, rótulo, número, dispositivo) × o que se deduz de um critério. O primeiro vira cartão; o segundo vira compreensão e, se couber, material de revisão (D24, aplicando a bifurcação da `metodo-professor` 1.2).
- **Eixo conteúdo × eixo questão (D25):** as duas naturezas de indicador do estado do aluno — onde ele trava *entendendo* (travamentos T#, bloco 1.1) × onde ele erra *decidindo sob pressão* (entradas E#, bloco 1.2). Um não prevê o outro, e o cruzamento entre eles é o que revela dúvida adiada.
- **Travamento (T#):** registro de ponto que o aluno não decodificou sozinho na leitura, com a carga (intrínseca × extrínseca) anotada. Três no mesmo ponto viram lacuna estrutural.
- **Densidade de travamento:** travamentos por volume lido (por dezena de páginas), o indicador do eixo conteúdo. Número absoluto não se compara entre sessões de tamanhos diferentes.
- **Arquivo de edições × artefato integral (D26):** lista de âncoras e trechos que descreve uma mudança × o documento completo já com a mudança aplicada. O primeiro é método interno de trabalho e nunca sai para outputs; só o segundo é entregável, e é o único que se sobe na base.
- **Caderno da disciplina:** arquivo único do Project-filho, com duas seções — estado do aluno e dossiê de banca.
- **Passe de promoção:** ritual periódico no Project-mãe em que regra amadurecida no caderno sobe para a skill e é podada do caderno.
- **Backlog do ateliê:** arquivo vivo do Project-mãe (inventário + fila de trabalho + fricções). Este documento aponta para ele; não repete seu conteúdo.
- **Código glosado × código nu:** citar o mecanismo antes e o código entre parênteses × largar `E12`/`P4` sozinho, ilegível fora do contexto que o gerou (D19).
- **Visual de ancoragem × visual-instrumento:** o que o aluno lê (Design System livre) × o que ele redesenha à mão na prova (cabe em A4, cor não carrega informação, sem dependência de layout ou software) — D20.
- **Mapa do sistema:** artefato estável de uma página que descreve o conjunto (camadas, ciclo de vida de um registro, quem escreve o quê, rotinas) + diagrama. Responde ao desconforto de legibilidade, não de orquestração (D18).
- **Fonte primária × fallback:** o material original do curso é sempre a fonte de conversão da apostila; o reduzido nunca alimenta a base do Project. PDF bruto é aceito como fallback temporário quando a conversão não aconteceu a tempo — nunca via permanente (D21).
- **Fonte fria × cópia em execução:** distinção introduzida pelo D22 e **revogada pelo D23**. Não há mais camada de pasta local nem hierarquia de desempate entre cópias: o artefato vive na cópia em execução (skill na conta, arquivo na base do Project) e o `outputs` é só correia de transmissão para baixar e re-subir (D14/D15).
- **Nome fixo × nome versionado (D27):** arquivo cujo nome nunca muda, com a versão só na linha de versão do documento, no commit e na tag × arquivo cujo nome carrega a versão (`-v8_8.md`), em que cada versão é um arquivo novo e o anterior precisa ser retirado à mão. O segundo é a metade do incidente de 2026-09-11 que o D26 não tinha coberto.
- **Repositório de histórico × fonte da verdade (D27):** o Git guarda o que já foi entregue, **abaixo** da cópia em execução × um repositório que manda sobre as demais cópias, que é o que o D18 recusou e o D27 continua recusando.
- **Escrita direta na base (D28):** a sessão grava o artefato na base do Project e lê de volta para conferir, em vez de gerar em `outputs` para o arquiteto re-subir. Vale onde a ferramenta existir; no chat web, ainda não verificado.
 
## Onde está o resto

**Inventário, fila de trabalho e fricções não moram aqui** (D17). Estão no **`backlog-atelie.md`**, na base de conhecimento do Project-mãe: versões de cada skill e professor, o que está na fila e por quê, e as notas de melhoria da 8 em diante.

Ao trabalhar neste ateliê: leia as decisões aqui (o *porquê*), e o backlog para saber o estado e o que fazer em seguida.
