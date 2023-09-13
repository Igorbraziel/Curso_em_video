lista1 = []
listaPares = []
listaImpares = []
while True:
    num = int(input('Digite um número: '))
    lista1.append(num)
    opção = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while opção not in 'SN':
        print('Tente novamente!', end = ' ')
        opção = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if opção == 'N':
        break
for i in range(0, len(lista1)):
    if lista1[i] % 2 == 0:
        listaPares.append(lista1[i])
    elif lista1[i] % 2 != 0:
        listaImpares.append(lista1[i])

print(f'A lista total digitada é {lista1}')
print(f'A lista de números ímpares é {listaImpares}')
print(f'A lista de números pares é {listaPares}')

