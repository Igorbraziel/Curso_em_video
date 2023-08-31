km = int(input('Digite o valor da distância da sua viagem: '))

if km >= 200:
    print('O valor da viagem será R$ {:.2f}'.format(km * 0.45))
else: 
    print('O valor da viagem será R$ {:.2f}'.format(km * 0.5))
    