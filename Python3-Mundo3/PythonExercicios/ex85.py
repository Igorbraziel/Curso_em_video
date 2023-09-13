pares = list()
impares = list()
total = list()
k1 = k2 = 0

for i in range(0, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

total.append(pares[:])
total.append(impares[:])
total[0].sort()
total[1].sort()

print('Os valores pares e ímpares em ordem crescente respectivamente são:')
print(total)
