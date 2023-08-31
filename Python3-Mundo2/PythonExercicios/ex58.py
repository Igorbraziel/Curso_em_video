from random import randint
from time import sleep

print('\=/' * 10)
print('VAMOS JOGAR!!')
print('\=/' * 10)
sleep(2)

print('Vou pensar em um número entre 0 e 10, PROCESSANDO...')
sleep(3)

computador = randint(0, 10)
jogador = -1
k = 0

while jogador != computador:
    jogador = int(input('Tente advinhar que número eu escolhi: '))
    if jogador > computador:
        print('Você errou, tente novamente!!')
        print('Dica: é um número menor que {}'.format(jogador))
    elif jogador < computador:
        print('Você errou, tente novamente!!')
        print('Dica: é um número maior que {}'.format(jogador))
    k += 1
print('Você acertou!!')
print('Eu escolhi o número {} e você precisou de {} tentativas para acertar'.format(computador, k))
