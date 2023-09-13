numeros = list()
matriz = list()
k = 1
c = 0
for i in range(0, 3):
    for j in range(0, 3):
        numeros.append(int(input(f'Digite o {k}º valor da matriz: ')))
        k += 1
    matriz.append(numeros[c:k])
    c += 3

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end = ' ')
    print()    

