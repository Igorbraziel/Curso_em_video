from time import sleep

def maior(*numeros):
    maior = 0
    for indice, valor in enumerate(numeros):
        if indice == 0 or valor > maior:
            maior = valor
    print('Os valores passados por parâmetro foram:')
    for valor in numeros:
        print(valor, end = ' ', flush = True)
        sleep(0.5)
    print(f'que totalizam {len(numeros)} valores')
    print(f'O maior valor passado por parâmetro foi {maior}')
    print('=-' * 40)
    sleep(1)

print('=-' * 40)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
