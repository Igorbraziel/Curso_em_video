frase = str(input('Digite uma frase: ')).strip()
nl = len(frase) - frase.count(' ')
frase1 = frase
lista = frase.split()
frase = ''.join(lista)
fim = len(frase) - 1
k = 0
j = 0
for i in range(fim, -1, -1):
    if frase[i] == frase[j]:
        k += 1
    j += 1
if k == nl:
    print('A frase ({}) É UM PALÍNDROMO'.format(frase1.upper()))
else:
    print('A frase ({}) NÃO É UM PALÍNDORMO'.format(frase1.upper()))
