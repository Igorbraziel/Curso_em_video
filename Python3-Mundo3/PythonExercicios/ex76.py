print('-' * 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-' *  40)
listagem = ('Computador', 5000, 
            'Notebook', 3000,
            'TV', 7000,
            'Bola de Futebol', 100,
            'Caneca', 20,
            'Caneta', 1.50)
for i in range(0, len(listagem), 2):
    print(listagem[i], end = '')
    k = len(listagem[i])
    while k < 25:
        print('.', end = '')
        k += 1
    print('R$', end = ' ')
    print(f'{listagem[i + 1]:>7.2f}')
print('-' *  40)