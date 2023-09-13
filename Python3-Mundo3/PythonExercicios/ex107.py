from utilidadesCeV import moedas

p = float(input('Digite o preço: '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'{moedas.moeda(p)} com um aumento de 10% equivale a {moedas.moeda(moedas.aumentar(p, 10))}')
print(f'{moedas.moeda(p)} com um desconto de 13% equivale a {moedas.moeda(moedas.diminuir(p, 13))}')