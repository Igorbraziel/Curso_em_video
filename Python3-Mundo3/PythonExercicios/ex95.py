jogador = dict()
time = list()
gols = list()
total = k = 0
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas o jogador {jogador["nome"].upper()} fez na temporada? '))
    for i in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida número {i + 1}? ')))
    for golPart in gols:
        total += golPart
    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = total
    total = 0
    jogador['aproveitamento'] = jogador['total'] / jogador['partidas']
    time.append(jogador.copy())
    while op not in 'SN':
        print('Tente novamente!')
        op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break
print('=-=' * 20)
print(f'{"Cod":>3}', f'{"Nome":<15}', f'{"Gols":<15}', f'{"Total":>5}')
print('-' * 60)
for i, j in enumerate(time):
    print(f'{i:>3}', end = ' ')
    print(f'{j["nome"]:<15}', end = '')
    print(f'{str(j["gols"]):<15}', end = '')
    print(f'{j["total"]:>5}')
print('-' * 60)
indice = 0
while True:
    indice = int(input('Deseja ver os dados de qual jogador? (999 para parar): '))
    if indice == 999:
        break
    if 0 <= indice < len(time):
        print('=-=' * 20)
        print(f'Levantamento do jogador {time[indice]["nome"]}:')
        for i, gol in enumerate(time[indice]['gols']):
            print(f'No jogo {i + 1} fez {gol} gols')
        print('=-=' * 20)
    else:
        print('DADOS INVÁLIDOS!!')

