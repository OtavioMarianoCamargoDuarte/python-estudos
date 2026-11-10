# Tratamento de Erros

## O que é Tratamento de Erros?

O tratamento de erros permite que o programa lide com situações inesperadas sem encerrar sua execução de forma abrupta.

Exemplos:

- Usuário digitar texto quando um número é esperado.
- Tentativa de divisão por zero.
- Acesso a uma posição inexistente de uma lista.

---

## Raise

A instrução `raise` é utilizada para lançar um erro manualmente.

Exemplo:

```python
if valor > saldo:
    raise ValueError("Saldo insuficiente.")
```

Quando essa linha é executada, o Python interrompe o fluxo normal e gera uma exceção.

---

## Try e Except

O bloco `try` é utilizado para executar um código que pode gerar erro.

O bloco `except` é utilizado para capturar e tratar esse erro.

Exemplo:

```python
try:
    conta1.sacar(1500)

except ValueError as erro:
    print(erro)
```

Quando ocorre um erro do tipo `ValueError`, o programa não é interrompido e o erro pode ser tratado adequadamente.

---

## Else

O bloco `else` é executado apenas quando nenhum erro ocorre dentro do bloco `try`.

Exemplo:

```python
try:
    valor = int(input("Digite um número: "))

except ValueError:
    print("Erro")

else:
    print("Sucesso")
```

Fluxo:

- Se houver erro → executa o `except`.
- Se não houver erro → executa o `else`.

---

## Finally

O bloco `finally` é executado independentemente de ocorrer erro ou não.

Exemplo:

```python
try:
    ...
except:
    ...
finally:
    print("Fim")
```

O código dentro do `finally` sempre será executado.

---

## Múltiplos Except

Um programa pode tratar diferentes tipos de erro.

Exemplo:

```python
try:
    numero = int(input())

except ValueError:
    print("Digite apenas números.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")
```

Cada tipo de erro pode receber um tratamento específico.

---

## Erros Comuns

### ValueError

Ocorre quando um valor possui um formato ou tipo inválido.

Exemplo:

```python
int("otavio")
```

Resultado:

```python
ValueError
```

---

### ZeroDivisionError

Ocorre quando tentamos dividir um número por zero.

Exemplo:

```python
10 / 0
```

Resultado:

```python
ZeroDivisionError
```

---

### IndexError

Ocorre quando tentamos acessar uma posição inexistente em uma lista.

Exemplo:

```python
numeros = [10, 20, 30]

print(numeros[5])
```

Resultado:

```python
IndexError
```

---

## Validação com Loop

Podemos combinar:

- while
- try
- except
- else

para repetir a entrada de dados até que o usuário informe um valor válido.

Exemplo:

```python
while True:

    try:
        idade = int(input("Digite sua idade: "))

    except ValueError:
        print("Digite apenas números.")

    else:
        break
```

Essa técnica é muito utilizada em sistemas reais.

---

## Ordem de Execução

Estrutura completa:

```python
try:
    ...

except:
    ...

else:
    ...

finally:
    ...
```

Fluxo:

- `try` → tenta executar o código.
- `except` → executa quando ocorre um erro.
- `else` → executa quando não ocorre erro.
- `finally` → executa sempre.

Representação visual:

```text
try
 │
 ├─ erro?
 │
 ├─ Sim ──► except
 │
 └─ Não ─► else
             │
             ▼
          finally
```

---

## Exemplo Completo

```python
while True:

    try:

        numero1 = float(input("Primeiro número: "))
        numero2 = float(input("Segundo número: "))

        resultado = numero1 / numero2

    except ValueError:

        print("Digite apenas números.")

    except ZeroDivisionError:

        print("Não é possível dividir por zero.")

    else:

        print(f"Resultado: {resultado}")
        break

    finally:

        print("Tentativa encerrada.")
```

Nesse exemplo utilizamos:

- while
- try
- except
- else
- finally
- ValueError
- ZeroDivisionError

---

## Resumo dos Conceitos Aprendidos

✅ Raise

✅ Try

✅ Except

✅ Else

✅ Finally

✅ ValueError

✅ ZeroDivisionError

✅ IndexError

✅ Múltiplos Except

✅ Validação com Loop

✅ Fluxo de Tratamento de Erros