lista = list()
for i in range(0, 5):
    lista.append(int(input(f'Digite o {i + 1}º valor: ')))
maior = max(lista)
menor = min(lista)

if lista.count(maior) > 1:
    print(f'O maior valor é {max(lista)} e ele está nas posições', end = ' ')
else:
    print(f'O maior valor é {max(lista)} e ele está na posição', end = ' ')
for i in range(0, len(lista)):
    if lista[i] == maior:
        print(f'{i}', end = ' ')
print()

if lista.count(menor) > 1:
    print(f'O maior valor é {min(lista)} e ele está nas posições', end = ' ')
else:
    print(f'O maior valor é {min(lista)} e ele está na posição', end = ' ')
for i in range(0, len(lista)):
    if lista[i] == menor:
        print(f'{i}', end = ' ')
print()


