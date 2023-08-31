import math
ângulo = float(input('Digite o valor do ângulo: '))
x = (math.pi * ângulo) / 180
seno = math.sin(x)
cosseno = math.cos(x)
tangente = math.tan(x)
print('O seno de {:.2f}º é {:.2f}\nO cosseno de {:.2f}º é {:.2f}\nA tangente de {:.2f} é {:.2f}'.format(ângulo, seno, ângulo, cosseno, ângulo, tangente))