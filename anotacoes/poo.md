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

## Atributos com __init__

O método `__init__` pode receber valores no momento da criação do objeto.

Exemplo:

```python
class Pessoa:

    def __init__(self, nome):
        self.nome = nome
```

Ao criar:

```python
pessoa1 = Pessoa("Otavio")
```

o atributo `nome` recebe o valor `"Otavio"`.

A instrução:

```python
self.nome = nome
```

armazena o valor recebido dentro do objeto.

## Exemplo Completo

```python
class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")
```

Uso:

```python
pessoa1 = Pessoa("Otavio")
pessoa2 = Pessoa("Maria")

pessoa1.apresentar()
pessoa2.apresentar()
```

Saída:

```text
Olá, meu nome é Otavio
Olá, meu nome é Maria
```

Neste exemplo são utilizados:

- Classe
- Objeto
- Atributo
- Método
- __init__
- self
```

## Métodos utilizando atributos

Os métodos podem acessar os atributos do próprio objeto utilizando `self`.

Exemplo:

```python
class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo}")
```

O método `mostrar_saldo()` utiliza o atributo `saldo` armazenado no objeto.