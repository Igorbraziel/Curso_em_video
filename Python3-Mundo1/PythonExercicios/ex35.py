n1 = float(input('Digite o primeito comprimento de reta: '))
n2 = float(input('Digite o segundo comprimento de reta: '))
n3 = float(input('Digite o terceiro comprimento de reta: '))

if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n2 + n1:
    print('ESSE \033[1;34mTRIÂNGULO\033[m PODE EXISTIR!!')
else:
    print('ESSE \033[1;34mTRIÂNGULO\033[m NÃO PODE EXISTIR!!')