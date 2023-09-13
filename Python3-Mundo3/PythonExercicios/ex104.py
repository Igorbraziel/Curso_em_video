def leiaInt(frase):
    x = input(f'{frase}')
    if x.isnumeric():
        x = int(x)
        print(f'O valor {x} é um valor numérico')
        return x
    else:
        print(f'\033[31m({x}) não é um valor numérico! digite novamente\033[m')
        x = leiaInt('Digite um valor numérico: ')
        return x


num = int(leiaInt('Digite um valor numérico: '))
print(f'Você digitou o valor {num}')