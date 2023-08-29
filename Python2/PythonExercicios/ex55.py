peso = float(input('Digite o 1º peso (KG): '))
maior = peso
menor = peso
for i in range(1, 5):
    peso = float(input('Digite o {}º peso (KG): '.format(i + 1)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso é {:.2f} KG'.format(maior))
print('O menor peso é {:.2f} KG'.format(menor))
