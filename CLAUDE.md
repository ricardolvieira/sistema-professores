# Sistema de Professores — repositório de histórico

Este repositório guarda os artefatos do meu sistema de estudos para concurso. **Não é
código** e **não é fonte da verdade**: o artefato vive na *cópia em execução* — skill na
conta Claude, arquivo na base de conhecimento do Project. Aqui fica o registro do que já
foi entregue, abaixo da cópia em execução, nunca acima dela.

O *porquê* de cada regra está em `atelie/decisoes-de-design.md`. Leia a decisão relevante
antes de propor mudança de estrutura ou de convenção. Se a mudança contrariar uma decisão
registrada, **aponte isso explicitamente em vez de seguir calado**.

## Convenções de arquivo

- Nome em **minúsculas, hífen entre palavras, sem acento e sem versão**.
  `decisoes-de-design.md` — nunca `decisoes-de-design-v8_10.md`, nunca `-810`.
- A versão fica **dentro** do documento (linha de versão sob o título), na mensagem do
  commit e na tag, sempre com **ponto**: `8.10`, nunca `8_10`.
- O caminho aqui **espelha** o caminho na base do Project, para o `git diff` ser
  comparável direto contra o que está subido. Não invente pasta para artefato que já tem
  lugar.
- Fim de linha **LF** em todo arquivo de texto, imposto pelo `.gitattributes` (D29).
  Não converta arquivo à mão: o Git converte no `git add`.

## Layout

| Pasta | O que guarda |
|---|---|
| `atelie/` | decisões, backlog, mapa do sistema, template do caderno |
| `skills/<nome>/` | `SKILL.md` e `scripts/` de cada skill |
| `professores/<disciplina>/` | prompt de estado, caderno, flashcards, notas de melhoria |

`professores/*/apostila/` é ignorada pelo Git: material de terceiro, grande e regenerável
a partir do PDF pela skill `conversao-apostila`.

## Ao mexer na estrutura

Criou pasta nova, mudou convenção ou acrescentou tipo de artefato? **Atualize o
`README.md` na mesma operação** — a tabela de layout e a seção de convenções. README
desatualizado é pior que ausente, porque é lido como verdade.

## Commits

- Um commit por entrega, com a versão na mensagem:
  `decisoes-de-design v8.10 (2026-09-16)`.
- **`git diff` antes de todo commit é verificação obrigatória**, não conferência
  opcional. É o passo que denuncia arquivo salvo no lugar errado antes de ele virar
  histórico.
- Repositório burro, por decisão: sem CI, sem workflow do GitHub, sem submódulo, sem
  branch além da `main`.
- **Sessão remota (pasta conectada ao Claude):** o ambiente não tem credencial do GitHub
  nem identidade Git. Faça o commit passando a identidade só no comando
  (`git -c user.name="Ricardo Lima Vieira" -c user.email="riclimavieira@gmail.com" commit`),
  sem gravar configuração, e deixe o `git push` para o Ricardo, no terminal do VS Code.
  Se o Git falhar com `unable to unlink` ou `index.lock`, falta permissão de exclusão na
  pasta: peça a permissão antes de insistir e remova o `index.lock` que a tentativa deixou.

## O que não fazer

- **Não edite o conteúdo dos artefatos** para corrigir formatação, ortografia ou
  estrutura. São cópias fiéis do que está em execução; divergência silenciosa entre as
  duas cópias é a falha mais cara que este sistema já teve.
- **Não gere arquivo de edições, patch ou delta como entregável.** Edição é método
  interno; o que circula é sempre o documento integral.
- **Não reconstrua artefato de memória.** Sem o arquivo íntegro em mãos, peça o arquivo.
