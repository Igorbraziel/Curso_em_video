from random import randint
from time import sleep

cartela = list()
jogo = list()

print('~=~' * 15)
print('''
                MEGA SENA
''')
print('~=~' * 15)

qtd = int(input('Quantos jogos você deseja gerar? '))

for i in range(0, qtd):
    for j in range(0, 6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1, 60)
        jogo.append(num)
    jogo.sort()
    cartela.append(jogo[:])
    jogo.clear()
print('~=~' * 15)
print(f'            SEUS {qtd} JOGOS             ')
print('~=~' * 15)

for i in range(0, qtd):
    print(f'Seu jogo número {i + 1} é: {cartela[i]}')
    sleep(1)
print('=-' * 7, '<=BOA SORTE!!!=>', '=-' * 7)