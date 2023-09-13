pessoas = list()
dados = dict()
media = k = 0
while True:
    dados['nome'] = str(input('Digite o seu nome: '))
    dados['sexo'] = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
    while dados['sexo'] not in 'MF':
        print('Tente novamente!', end = ' ')
        dados['sexo'] = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
    dados['idade'] = int(input('Digite a sua idade: '))
    pessoas.append(dados.copy())
    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while op not in 'SN':
        print('Opção inválida, digite novemente!')
        op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break
print(':==' * 20)
print(f'O total de pessoas cadastradas foi {len(pessoas)}')
for p in pessoas:
    media += p['idade']
media /= len(pessoas)
print(f'A média de idade do grupo é de {media:.2f}')
print('As mulheres do grupo são:', end = ' ')
for i, p in enumerate(pessoas):
    if k == 0 and p['sexo'] == 'F':
        print(f'{p["nome"]}', end = '')
        k = 1
    elif p['sexo'] == 'F':
        print(f', {p["nome"]}', end = '')
print()
print('As pessoas com a idade acima da média são:', end = ' ')
k = 0
for i, p in enumerate(pessoas):
    if k == 0 and p['idade'] >= media:
        print(f'{p["nome"]}', end = '')
        k = 1
    elif p['idade'] >= media:
        print(f', {p["nome"]}', end = '')
print()
print(':==' * 20)

