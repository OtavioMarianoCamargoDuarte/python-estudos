# Programação Orientada a Objetos

## O que é POO?

POO significa Programação Orientada a Objetos.

Ela permite representar objetos do mundo real através de código.

Exemplos:

- Pessoa
- Carro
- Conta Bancária
- Produto

---

## Classe

Uma classe é um molde para criar objetos.

Exemplo:

```python
class Pessoa:
    pass
```

Neste momento a classe existe, mas nenhum objeto foi criado.

---

## Pass

A palavra reservada `pass` indica que nenhum código será executado naquele bloco por enquanto.

## Objeto

Um objeto é uma instância de uma classe.

Exemplo:

```python
class Pessoa:
    pass

pessoa1 = Pessoa()
```

Neste exemplo:

- Pessoa é a classe.
- pessoa1 é um objeto.

A classe funciona como um molde.

O objeto é criado a partir desse molde.

## Atributo

Um atributo é uma informação armazenada dentro de um objeto.

Exemplo:

```python
pessoa1.nome = "Otavio"
```

Neste caso:

- pessoa1 é o objeto.
- nome é o atributo.
- Otavio é o valor do atributo.

## Método

Um método é uma ação que um objeto pode executar.

Exemplo:

```python
class Pessoa:

    def apresentar(self):
        print("Olá!")
```

Neste caso:

- apresentar é um método.
- Métodos representam comportamentos ou ações dos objetos.

## Método __init__

O método `__init__` é executado automaticamente quando um objeto é criado.

Exemplo:

```python
class Pessoa:

    def __init__(self):
        print("Pessoa criada!")
```

Ao executar:

```python
pessoa1 = Pessoa()
```

o método `__init__` é chamado automaticamente.

Sua função é inicializar o objeto.

## Self

O parâmetro `self` representa o próprio objeto.

Exemplo:

```python
class Pessoa:

    def __init__(self):
        print(self)
```

Quando um objeto é criado:

```python
pessoa1 = Pessoa()
```

o Python envia automaticamente esse objeto para o parâmetro `self`.

Cada objeto possui seu próprio `self`.