try:
    valor = int(input('Digite um número: '))

except ValueError:
    print('Você não digitou um número.')

else:
    print(f'Número digitado: {valor}')