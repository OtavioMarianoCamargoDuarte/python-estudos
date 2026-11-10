while True:

    try:

        numero1 = float(input('Primeiro número: '))
        numero2 = float(input('Segundo número: '))

        resultado = numero1 / numero2

    except ValueError:

        print('Digite apenas números.')

    except ZeroDivisionError:
        print('Não é possível dividir por zero.')

    else:

        print(f'Resultado: {resultado}')
        break

    finally:
        print('Tentativa encerrada.')