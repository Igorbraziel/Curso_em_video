n = int(input('Digite um número inteiro e veja sua tabuada: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(n, i, n * i))