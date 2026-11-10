try:

    numeros = [10, 20, 30]

    indice = int(input('Digite um índice: '))

    print(numeros[indice])

except ValueError:
    print('Digite apenas números.')

except IndexError:
    print('Índice não existe.')

finally:
    print('Programa encerrado.')