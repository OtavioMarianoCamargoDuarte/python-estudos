try:

    numero = int(input('Digite um número: '))
    resultado = 10 / numero

except ValueError:
    print('Digite apenas números.')

except ZeroDivisionError:
    print('Não é possível dividir por zero.')

else:
    print(f'Resultado: {resultado}')

finally:
    print('Operação encerrada.')