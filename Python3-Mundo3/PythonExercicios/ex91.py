from random import randint
from time import sleep
from operator import itemgetter
dados = dict()
dados['jogador1'] = randint(1, 6)
dados['jogador2'] = randint(1, 6)
dados['jogador3'] = randint(1, 6)
dados['jogador4'] = randint(1, 6)
i = t = 0
for k, v in dados.items():
    print(f'O {k} tirou {v}')
    if i == 0 or v > maior:
        maior = v
        indice = k
    i += 1
    sleep(1)
ranking = sorted(dados.items(), key = itemgetter(1), reverse = True)
for jogo in ranking:
    print(f'{t + 1}º Lugar: {jogo[0]} que tirou {jogo[1]}')
    t += 1

