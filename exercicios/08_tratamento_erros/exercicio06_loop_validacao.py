while True:

    try:

        idade = int(input('Digite sua idade: '))

    except ValueError:

        print('Digite apenas números.')

    else:

        print(f'Sua idade é {idade} anos.')
        break

print('Cadastro finalizado.')