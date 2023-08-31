n = 0
soma = 0
k = 0
while n != 999:
    n = int(input('Digite um número, PARA PARAR DIGITE -> (999): '))
    soma += n
    k += 1
soma -= 999
k -= 1
print('Foram lidos {} números e a soma entre eles é {}'.format(k, soma))