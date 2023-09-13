def jogador(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gols no campeonato!')


nome = str(input('Nome do Jogador: ')).strip()
numGol = str(input('Número de gols: ')).strip()
if numGol.isnumeric() == True:
    numGol = int(numGol)
else:
    numGol = int(0)
if nome == '':
    nome = '<desconhecido>'
jogador(nome, numGol)
