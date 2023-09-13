from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

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
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')


