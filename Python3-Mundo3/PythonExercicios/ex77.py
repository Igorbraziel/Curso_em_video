brasileirao = ('Botafogo',
               'Palmeiras',
               'Gremio',
               'Flamengo',
               'Fluminense',
               'Bragantino',
               'Athletico-PR',
               'Fortaleza',
               'Atletico-MG',
               'Cuiaba',
               'Sao Paulo',
               'Cruzeiro',
               'Corinthians',
               'Internacional',
               'Goias',
               'Bahia',
               'Santos',
               'Vasco',
               'Coritiba',
               'America-MG')
for i in range(0, len(brasileirao)):
    print(f'Na palavra {brasileirao[i].upper()} temos as vogais:', end = ' ')
    for j in range(0, len(brasileirao[i])):
        if brasileirao[i][j].upper() in 'AEIOU':
            print(f'{brasileirao[i][j].upper()}', end = ' ')
    print()
