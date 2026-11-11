# Programação Orientada a Objetos (POO)

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

Uma classe é um molde utilizado para criar objetos.

Exemplo:

```python
class Pessoa:
    pass
```

Neste momento a classe existe, mas nenhum objeto foi criado.

---

## Pass

A palavra reservada `pass` indica que nenhum código será executado naquele bloco por enquanto.

Exemplo:

```python
class Pessoa:
    pass
```

É utilizada quando ainda não implementamos a lógica da classe ou função.

---

## Objeto

Um objeto é uma instância criada a partir de uma classe.

Exemplo:

```python
class Pessoa:
    pass

pessoa1 = Pessoa()
```

Neste exemplo:

- `Pessoa` é a classe.
- `pessoa1` é o objeto.

A classe funciona como um molde.

O objeto é criado a partir desse molde.

---

## Atributo

Um atributo é uma informação armazenada dentro de um objeto.

Exemplo:

```python
pessoa1.nome = "Otavio"
```

Neste caso:

- `pessoa1` é o objeto.
- `nome` é o atributo.
- `"Otavio"` é o valor armazenado.

---

## Método

Um método é uma ação que um objeto pode executar.

Exemplo:

```python
class Pessoa:

    def apresentar(self):
        print("Olá!")
```

Neste caso:

- `apresentar()` é um método.
- Métodos representam comportamentos ou ações dos objetos.

---

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

---

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

---

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

---

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

Neste exemplo foram utilizados:

- Classe
- Objeto
- Atributo
- Método
- `__init__`
- `self`

---

## Métodos Utilizando Atributos

Os métodos podem acessar atributos do próprio objeto utilizando `self`.

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

---

## Métodos Podem Alterar Atributos

Os métodos não apenas consultam informações, mas também podem modificar os atributos do objeto.

Exemplo:

```python
def depositar(self, valor):
    self.saldo += valor
```

Ao executar:

```python
conta.depositar(500)
```

o saldo armazenado dentro do objeto é atualizado.

---

## Validação em Métodos

Os métodos podem conter regras para impedir operações inválidas.

Exemplo:

```python
def sacar(self, valor):

    if valor > self.saldo:
        print("Saldo insuficiente.")
        return

    self.saldo -= valor
```

Neste exemplo:

- O saque só ocorre se houver saldo suficiente.
- Caso contrário, o método é interrompido.
- O saldo permanece inalterado.

Validações são utilizadas para proteger os dados do objeto contra alterações incorretas.

---

## Resumo dos Conceitos Aprendidos

✅ Classe

✅ Objeto

✅ Atributo

✅ Método

✅ `__init__`

✅ `self`

✅ Métodos utilizando atributos

✅ Métodos alterando atributos

✅ Validações

✅ Regras de negócio

## Atributo Protegido

Por convenção, atributos que começam com `_` são considerados internos da classe.

Exemplo:

```python
self._nome = nome
```

O Python permite o acesso, mas sinaliza que esse atributo não deveria ser alterado diretamente fora da classe.

Essa técnica é utilizada como primeiro passo para o encapsulamento.

## Property

O decorator `@property` permite acessar métodos como se fossem atributos.

Exemplo:

```python
class Pessoa:

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
```

Uso:

```python
pessoa.nome
```

Mesmo sendo um método internamente, ele é utilizado como um atributo.

## Setter

O setter permite validar alterações em um atributo.

Exemplo:

```python
@nome.setter
def nome(self, novo_nome):

    if not novo_nome:
        print("Nome inválido.")
        return

    self._nome = novo_nome
```

O setter é executado automaticamente quando fazemos:

```python
pessoa.nome = "Maria"
```

Ele permite verificar se o novo valor é válido antes de alterar o atributo.

## Método Especial __str__

O método `__str__()` é utilizado para definir como um objeto será exibido quando usamos a função `print()`.

Sem `__str__()`:

```python
class Pessoa:

    def __init__(self, nome):
        self._nome = nome


pessoa = Pessoa("Otavio")

print(pessoa)
```

Saída:

```text
<__main__.Pessoa object at 0x000001F2A4B8E710>
```

Essa saída não é amigável para o usuário.

---

Com `__str__()`:

```python
class Pessoa:

    def __init__(self, nome):
        self._nome = nome

    def __str__(self):
        return f"Pessoa: {self._nome}"
```

Uso:

```python
pessoa = Pessoa("Otavio")

print(pessoa)
```

Saída:

```text
Pessoa: Otavio
```

---

### Funcionamento

Quando utilizamos:

```python
print(pessoa)
```

o Python procura automaticamente pelo método:

```python
__str__()
```

Se ele existir, o valor retornado será exibido.

Se não existir, o Python exibirá uma representação padrão do objeto na memória.

---

### Vantagens

- Exibir informações mais amigáveis.
- Facilitar a leitura durante testes.
- Melhorar a depuração do código.
- Tornar objetos mais fáceis de entender ao usar `print()`.

---

### Exemplo com Conta Bancária

```python
class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"{self.titular} - Saldo: R$ {self.saldo}"
```

Uso:

```python
conta = ContaBancaria("Otavio", 1000)

print(conta)
```

Saída:

```text
Otavio - Saldo: R$ 1000
```