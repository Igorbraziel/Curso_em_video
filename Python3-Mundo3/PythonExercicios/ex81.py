lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    opção = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while opção not in 'SN':
        print('Tente novamente!', end = ' ')
        opção = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if opção == 'N':
        break
print(f'A quantidade de números digitados foram {len(lista)}')
lista.sort(reverse = True)
print(f'A lista de valores ordenada de forma decrescente é {lista}')
if 5 in lista:
    print(f'O valor 5 foi encontrado na posição {lista.index(5)}')
else:
    print('O valor 5 não foi encontrado na lista')