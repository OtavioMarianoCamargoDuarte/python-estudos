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