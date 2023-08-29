preço = float(input('Digite o preço do produto a ser compro: R$'))

print('Digite 1 para:')
print('-Pagamento à vista ou cheque')
print()

print('Digite 2 para:')
print('-Pagamento à vista no cartão')
print()

print('Digite 3 para:')
print('-Pagamento em até 2x no cartão')
print()

print('Digite 4 para:')
print('-Pagamento de 3x ou mais no cartão')
print()

n = int(input('Sua escolha: '))

if n == 1:
    preço = preço - (10/100 * preço)
elif n == 2:
    preço = preço - (5/100 * preço)
elif n == 3:
    preço = preço
elif n == 4:
    preço = preço + (20/100 * preço)

print('O valor a ser pago pelo produto será de R${:.2f}'.format(preço))