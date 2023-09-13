jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas o jogador {jogador["nome"].upper()} fez na temporada? '))
for i in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida número {i + 1}? ')))
for golPart in gols:
        total += golPart
jogador['gols'] = gols[:]
jogador['total'] = total
jogador['aproveitamento'] = jogador['total'] / jogador['partidas']
print(jogador)
print('==' * 20)
for key, value in jogador.items():
      print(f'A chave {key} tem o valor {value}')
print('##' * 20)
for indice, value in enumerate(jogador['gols']):
      print(f'O jogador {jogador["nome"].capitalize()} tem {value} gols na partida {indice + 1}')
print('==' * 20)
print(f'O total de gols de {jogador["nome"].upper()} na temporada foi {jogador["total"]}')
print(f'A média de gols por partida de {jogador["nome"].upper()} na temporada foi de {jogador["aproveitamento"]}')