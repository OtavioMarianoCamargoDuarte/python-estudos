try:
    valor = int(input('Digite um número: '))

except ValueError:
    print('Valor inválido.')

else:
    print(f'Valor digitado: {valor}')

finally:
    print('Fim do programa.')