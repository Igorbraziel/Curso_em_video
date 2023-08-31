dias = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos Kilômetros foram percorridos? '))
preçoF = (km * 0.15) + (60 * dias)
print('O total a pagar é {:.2f}'.format(preçoF))