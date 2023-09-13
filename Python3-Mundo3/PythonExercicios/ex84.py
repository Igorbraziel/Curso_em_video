pessoas = list()
dados = list()
k = 0
while True:
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(float(input('Digite o seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    while True:
        opção = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if opção in 'SN':
            break
        print('Tente novamente!', end = ' ')
    if opção == 'N':
        break

print(f'O total de pessoas cadastradas foram {len(pessoas)}')

for i in range(0, len(pessoas)):
    if i == 0:
        maior = menor = pessoas[i][1]
    elif pessoas[i][1] > maior:
        maior = pessoas[i][1]
    elif pessoas[i][1] < menor:
        menor = pessoas[i][1]

print(f'O maior peso foi de {maior:.2f}KG. As pessoas que possuem esse peso são: ', end = '')
for i in range(0, len(pessoas)):
    if pessoas[i][1] == maior and k == 0:
        print(f'{pessoas[i][0]}', end = '')
        k = 1
    elif pessoas[i][1] == maior and k > 0:
        print(f', {pessoas[i][0]}', end = '')
k = 0
print()

print(f'O menor peso foi de {menor:.2f}KG. As pessoas que possuem esse peso são: ', end = '')
for i in range(0, len(pessoas)):
    if pessoas[i][1] == menor and k == 0:
        print(f'{pessoas[i][0]}', end = '')
        k = 1
    elif pessoas[i][1] == menor and k > 0:
        print(f', {pessoas[i][0]}', end = '')
print()

