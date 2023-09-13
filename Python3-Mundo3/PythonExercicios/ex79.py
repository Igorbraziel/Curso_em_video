lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    c = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while c not in 'SN':
        print('Digite novamente!')
        c = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if c == 'N':
        break
lista.sort()
print(lista)