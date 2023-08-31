from random import randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)

tupla = (n1, n2, n3, n4, n5)
print('Os valores sorteados foram:', end = ' ')
for i in range(0, len(tupla)):
    print(f'{tupla[i]}', end = '  ')
    if i == 0:
        menor = tupla[i]
        maior = tupla[i]
    elif tupla[i] > maior:
        maior = tupla[i]
    elif tupla[i] < menor:
        menor = tupla[i]
print()
print(f'O maior valor sorteado foi o {maior}')
print(f'O menor valor sorteado foi o {menor}')


