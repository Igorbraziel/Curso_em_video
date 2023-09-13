lista = list()
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0:
        lista.append(n)
        print('Adicionado no início da lista')
    else:
        for j in range(0, len(lista)):
            if n <= lista[j]:
                lista.insert(j, n)
                print(f'Adicionado na posição {j}')
                break
            elif j == len(lista) - 1:
                lista.insert(j + 1, n)
                print('Adiconado ao final da lista')
                break
print(lista)