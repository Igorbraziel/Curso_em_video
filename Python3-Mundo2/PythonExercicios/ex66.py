soma = k = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    k += 1
print(f'a soma é {soma} e {k} números foram lidos')