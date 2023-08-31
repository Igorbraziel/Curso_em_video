nome = input('Digite seu nome completo: ').strip()

lista = nome.split()

print('Seu primeiro nome é {}'.format(lista[0].capitalize()))

print('Seu último nome é {}'.format(lista[len(lista) - 1].capitalize()))