numeros = list()
matriz = list()
k = 1
c = somaPar = somaCol = 0
for i in range(0, 3):
    for j in range(0, 3):
        numeros.append(int(input(f'Digite o {k}º valor da matriz: ')))
        k += 1
    matriz.append(numeros[c:k])
    c += 3
print('=-=' * 15)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]}]', end = ' ')
        if matriz[i][j] % 2 == 0:
            somaPar += matriz[i][j]
        if j == 2:
            somaCol += matriz[i][j]
        if i == 1 and j == 0:
            maior = matriz[i][j]
        elif i == 1 and matriz[i][j] > maior:
            maior = matriz[i][j]
    print()
print('=-=' * 15)
print(f'A soma de todos os valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaCol}')
print(f'O maior valor da segunda linha é {maior}')
                