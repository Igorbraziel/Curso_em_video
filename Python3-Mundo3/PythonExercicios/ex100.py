from random import randint
from time import sleep


def sorteia(sorteados):
    for i in range(0, 5):
        sorteados.append(randint(1, 100))
    print(f'Os números sorteados foram: {sorteados}')


def somaPares(numeros):
    k = 0
    soma = 0
    print('=-' * 40)
    print('Os números pares são:')
    for num in numeros:
        if num % 2 == 0 and k == 0:
            print(f'{num}', end = '', flush = True)
            soma += num
            sleep(0.5)
            k = 1
        elif num % 2 == 0:
            print(f', {num}', end = '', flush = True)
            soma += num
            sleep(0.5)
    print()
    print(f'A soma dos valores pares é {soma}')
    print('=-' * 40)


lista = list()
sorteia(lista)
somaPares(lista)