brasileirao = ('Botafogo',
               'Palmeiras',
               'Grêmio',
               'Flamengo',
               'Fluminense',
               'Bragantino',
               'Athletico-PR',
               'Fortaleza',
               'Atlético-MG',
               'Cuiabá',
               'São Paulo',
               'Cruzeiro',
               'Corinthians',
               'Internacional',
               'Goiás',
               'Bahia',
               'Santos',
               'Vasco',
               'Coritiba',
               'América-MG')
print('Os primeiros 5 colocados do brasileirão são:')
for i in range(0, 5):
    print(f'{1 + i} - {brasileirao[i]}')
print('Os times que estão no Z4 do brasileirão são:')
for i in range(16, 20):
    print(f'{1 + i} - {brasileirao[i]}')
alfa = sorted(brasileirao)
print('Lista dos times em ordem alfabética:')
for i in range(0, 20):
    print(f'{i + 1} - {alfa[i]}')
print('Qual a colocação do Palmeiras?')
print(f'2º colocado - {brasileirao[1]}')