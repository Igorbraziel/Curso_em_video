n1 = int(input('Digite o primeiro valor a ser lido: '))
n2 = int(input('Digite o segundo valor a ser lido: '))
n3 = int(input('Digite o terceiro valor a ser lido: '))
n4 = int(input('Digite o quarto valor a ser lido: '))
numeros = (n1, n2, n3, n4)
k9 = 0
k = 0
for i in range(0, len(numeros)):
    if numeros[i] == 9:
        k9 += 1
    if k == 0 and numeros[i] == 3:
        indice = i + 1
        k += 1
print(f'O número 9 apareceu {k9} vezes')
if k > 0:
    print(f'O número 3 foi encontrado pela primeira vez na {indice}ª posição')
else:
    print('O número 3 não foi encontrado nenhuma vez')
k = 0

for i in range(0, len(numeros)):
    if k == 0 and numeros[i] % 2 == 0:
        print('Os valores pares encontrados foram:', end = ' ')
        print(f'{numeros[i]}', end = ' ')
        k += 1
    elif numeros[i] % 2 == 0:
        print(f'{numeros[i]}', end = ' ')
