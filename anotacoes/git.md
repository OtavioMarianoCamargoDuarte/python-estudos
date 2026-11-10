# Git

## O que é Git?

Git é um sistema de controle de versão utilizado para acompanhar alterações em arquivos e projetos.

Ele permite salvar diferentes versões do código e voltar para versões anteriores quando necessário.

---

## O que é um Repositório?

Um repositório é uma pasta que está sendo monitorada pelo Git.

Para criar um repositório:

```bash
git init
```

Esse comando cria uma pasta oculta chamada `.git`, responsável por armazenar todo o histórico do projeto.

---

## Verificando o Status do Projeto

Para verificar a situação atual dos arquivos:

```bash
git status
```

Possíveis estados:

- Untracked: arquivo ainda não monitorado pelo Git.
- Staged: arquivo preparado para o próximo commit.
- Commitado: arquivo salvo no histórico do Git.

---

## Adicionando Arquivos

Para preparar arquivos para um commit:

```bash
git add .
```

O ponto (`.`) significa que todos os arquivos alterados serão adicionados.

---

## Criando um Commit

Um commit é uma fotografia do projeto em determinado momento.

Exemplo:

```bash
git commit -m "Cria estrutura inicial de anotações"
```

Boas práticas:

- Mensagens curtas.
- Mensagens objetivas.
- Descrever o que foi feito.

Exemplos:

```bash
git commit -m "Adiciona exercícios de POO"
git commit -m "Corrige validação de preço"
git commit -m "Atualiza documentação"
```

---

## Consultando o Histórico

Para visualizar os commits realizados:

```bash
git log --oneline
```

Exemplo:

```bash
519d883 Cria estrutura inicial de anotações
```

Cada commit possui um identificador único.

---

## Fluxo Básico do Git

O fluxo mais comum é:

```bash
git status
git add .
git commit -m "Descrição da alteração"
```

Mais tarde, quando o projeto estiver conectado ao GitHub:

```bash
git push
```

---

## O que aprendi na prática

✅ Instalar e verificar o Git

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

✅ Entender os conceitos:

- Repositório
- Commit
- Histórico
- Staging Area
- Arquivos rastreados
- Arquivos não rastreados

---

## Observações

- O Git rastreia arquivos.
- O Git não rastreia pastas vazias.
- A pasta `.git` guarda todo o histórico do projeto.
- Um commit é uma fotografia do projeto em um determinado momento.

