num = str(input('Digite um número entre 0 e 9999: '))

print('Resolução com números:')

num = int(num)
uni = num % 10
dez = ((num % 100) - uni)
cen = ((num % 1000) - (uni + dez))
mil = num - (uni + dez + cen)

dez = dez / 10
cen = cen / 100
mil = mil / 1000

print('Unidade: {}'.format(int(uni)))
print('Dezena: {}'.format(int(dez)))
print('Centena: {}'.format(int(cen)))
print('Milhar: {}'.format(int(mil)))

print('Resolução com strings:')

num = str(num)

lista = num.strip()

if len(lista) == 4:
    print('Unidade: {}'.format(lista[3]))
    print('Dezena: {}'.format(lista[2]))
    print('Centena: {}'.format(lista[1]))
    print('Milhar: {}'.format(lista[0]))
elif len(lista) == 3:
    print('Unidade: {}'.format(lista[2]))
    print('Dezena: {}'.format(lista[1]))
    print('Centena: {}'.format(lista[0]))
    print('Milhar: 0')
elif len(lista) == 2:
    print('Unidade: {}'.format(lista[1]))
    print('Dezena: {}'.format(lista[0]))
    print('Centena: 0')
    print('Milhar: 0')
elif len(lista) == 1:
    print('Unidade: {}'.format(lista[0]))
    print('Dezena: 0')
    print('Centena: 0')
    print('Milhar: 0')
