from math import sqrt, pow
catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = sqrt(pow(catetoOposto, 2) + pow(catetoAdjacente, 2))
print('O valor da hipotenusa do seu triângulo retângulo é {:.2f}'.format(hipotenusa))