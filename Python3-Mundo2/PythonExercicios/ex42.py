r1 = float(input('Digite o primeiro comprimento de reta: '))
r2 = float(input('Digite o segundo comprimento de reta: '))
r3 = float(input('Digite o terceiro comprimento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Seu triângulo pode existir!!')
    if r1 == r2 and r2 == r3:
        print('SEU TRIÂNGULO É EQUILÁTERO!!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('SEU TRIÂNGULO É ISÓCELES!!')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('SEU TRIÂNGULO É ESCALENO!!')
else:
    print('Seu triângulo não pode existir!!')
    

    

    