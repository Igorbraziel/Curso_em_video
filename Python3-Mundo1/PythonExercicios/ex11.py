largura = float (input('Digite a largura da sua parede em metros: '))

altura = float (input('Digite a altura da sua parede em metros: '))

area = altura * largura

tinta = area / 2

print('A área da sua parede é de {:.2f}m² e serão necessários {:.2f} litros de tinta para pinta-la'.format(area, tinta))


