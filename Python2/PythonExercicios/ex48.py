soma = 0

for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        soma += i
print('A soma de todos os números ímpares e multiplos de 3 entre 1 e 500 é {}'.format(soma))