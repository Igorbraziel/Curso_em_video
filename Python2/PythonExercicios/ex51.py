a1 = float(input('Digite o primeiro termo de sua PA (Progressão aritmética): '))
r = float(input('Digite a razão de sua PA: '))
for i in range(0, 10):
    print('{}º termo: {:.2f} '.format(i + 1, a1))
    a1 += r