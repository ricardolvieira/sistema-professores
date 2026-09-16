# Sistema de Professores — repositório de histórico

Histórico e backup dos artefatos do sistema de estudos. **Não é fonte da verdade**
(D27): o artefato vive na cópia em execução — skill na conta, arquivo na base do
Project. Aqui fica o registro do que já foi entregue.

## Layout

| Pasta | O que guarda | Cópia em execução |
|---|---|---|
| `atelie/` | decisões, backlog, mapa, template do caderno, instruções | base do Project "Mãe dos professores" |
| `skills/<nome>/` | `SKILL.md` e `scripts/` de cada skill | skill instalada na conta |
| `professores/<disciplina>/` | prompt de estado, caderno, flashcards, notas de melhoria | base do Project-filho |

O caminho aqui espelha o caminho na base, para o diff ser comparável.

## Convenções

- Nome de arquivo: minúsculas, hífen entre palavras, sem acento, **sem versão**.
- A versão fica na linha de versão do documento, na mensagem do commit e na tag,
  sempre com ponto (`8.9`).
- Um `commit` e um `push` por entrega. Sem CI, sem hooks, sem branches de feature.
- `git diff` antes de todo commit é verificação obrigatória, não opcional.

## Apostilas

`professores/*/apostila/` é ignorada pelo Git: material de terceiro, grande e
regenerável a partir do PDF pela skill `conversao-apostila`.

O porquê de tudo está em `atelie/decisoes-de-design.md`.
