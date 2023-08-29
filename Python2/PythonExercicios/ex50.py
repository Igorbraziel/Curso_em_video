soma = 0
k = 0
for i in range(0, 6):
    n = int(input('Digite o {}º número: '.format(i + 1)))
    if n % 2 == 0:
        soma += n
        k += 1
print('A soma de todos os {} valores pares digitados é: {}'.format(k, soma))