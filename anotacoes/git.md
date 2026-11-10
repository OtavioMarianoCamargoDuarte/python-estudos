# Git

## O que é Git?

Git é um sistema de controle de versão utilizado para acompanhar alterações em arquivos e projetos.

Ele permite salvar diferentes versões do código e recuperar versões anteriores quando necessário.

---

## O que é um Repositório?

Um repositório é uma pasta monitorada pelo Git.

Para criar um repositório:

```bash
git init
```

Esse comando cria uma pasta oculta chamada:

```text
.git
```

Essa pasta guarda todo o histórico do projeto.

---

## Verificando o Status

Para verificar a situação atual do projeto:

```bash
git status
```

Possíveis estados:

### Untracked

Arquivos que existem no computador, mas ainda não são monitorados pelo Git.

### Staged

Arquivos preparados para entrar no próximo commit.

### Commitado

Arquivos salvos no histórico do Git.

---

## Adicionando Arquivos

Para adicionar arquivos ao Staging Area:

```bash
git add .
```

O ponto (`.`) significa adicionar todas as alterações da pasta atual.

---

## O que é um Commit?

Um commit é uma fotografia do projeto em um determinado momento.

Exemplo:

```bash
git commit -m "Cria estrutura inicial de estudos"
```

Boas práticas:

- Mensagens curtas
- Mensagens objetivas
- Descrever o que foi feito

Exemplos:

```bash
git commit -m "Adiciona exercícios de POO"
git commit -m "Corrige validação da classe Conta"
git commit -m "Atualiza documentação"
```

---

## Histórico de Commits

Para visualizar o histórico:

```bash
git log --oneline
```

Exemplo:

```text
519d883 Cria estrutura inicial de anotações
```

Cada commit possui um identificador único.

---

## Branch

Uma branch é uma linha de desenvolvimento.

A branch principal normalmente se chama:

```text
main
```

ou

```text
master
```

Verificar a branch atual:

```bash
git branch
```

Ver todas as branches:

```bash
git branch -a
```

No meu projeto atualmente:

```text
master
```

---

## Remote

Um remote é um repositório armazenado em outro local, normalmente no GitHub.

Verificar remotes configurados:

```bash
git remote -v
```

Adicionar um remote:

```bash
git remote add origin URL_DO_REPOSITORIO
```

No meu projeto:

```text
origin
```

é o apelido do repositório hospedado no GitHub.

---

## Push

Push envia os commits locais para o GitHub.

Primeiro envio:

```bash
git push -u origin master
```

Depois:

```bash
git push
```

---

## Fluxo Básico do Git

Fluxo mais utilizado no dia a dia:

```bash
git status
git add .
git commit -m "Descrição da alteração"
git push
```

---

## O que Aprendi

✅ Instalar o Git

```bash
git --version
```

✅ Criar um repositório

```bash
git init
```

✅ Verificar status

```bash
git status
```

✅ Adicionar arquivos

```bash
git add .
```

✅ Criar commits

```bash
git commit -m "mensagem"
```

✅ Visualizar histórico

```bash
git log --oneline
```

✅ Verificar branches

```bash
git branch
```

✅ Verificar remotes

```bash
git remote -v
```

✅ Entender os conceitos de:

- Repositório
- Commit
- Histórico
- Branch
- Remote
- Push
- Staging Area
- Arquivos rastreados
- Arquivos não rastreados

---

## Observações Importantes

- O Git rastreia arquivos.
- O Git não rastreia pastas vazias.
- A pasta `.git` guarda todo o histórico do projeto.
- Um commit é uma fotografia do projeto.
- O Git funciona localmente mesmo sem GitHub.
- O GitHub é utilizado para armazenar os repositórios na nuvem.