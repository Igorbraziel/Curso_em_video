a1 = float(input('Digite o primeiro termo de sua PA(Progressão aritmética): '))
r = float(input('Digite a razão de sua PA: '))
i = 1
while i <= 10:
    print('{}º termo da PA: {:.2f}'.format(i, a1))
    a1 = a1 + r
    i += 1