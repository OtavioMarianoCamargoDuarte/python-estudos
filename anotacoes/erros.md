# Tratamento de Erros

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

- Se houver erro → executa o except.
- Se não houver erro → executa o else.

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

## Múltiplos Except

Um programa pode tratar diferentes tipos de erro.

Exemplo:

```python
except ValueError:
```

Utilizado quando um valor inválido é informado.

```python
except ZeroDivisionError:
```

Utilizado quando ocorre uma divisão por zero.

Cada tipo de erro pode receber um tratamento específico.

## Erros Comuns

### ValueError

Ocorre quando um valor possui um tipo inválido.

Exemplo:

```python
int("otavio")
```

---

### ZeroDivisionError

Ocorre quando tentamos dividir por zero.

Exemplo:

```python
10 / 0
```

---

### IndexError

Ocorre quando tentamos acessar uma posição inexistente em uma lista.

Exemplo:

```python
numeros = [10, 20, 30]

print(numeros[5])
```

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
        idade = int(input())

    except ValueError:
        print("Erro")

    else:
        break
```

Essa técnica é muito utilizada em sistemas reais.
