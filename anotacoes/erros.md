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