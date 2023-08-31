num = int(input('Digite um número inteiro para ver seu fatorial: '))
n = num
fat = 1
print('{}! ='.format(num), end = ' ')
while num > 0:
    fat = fat * num
    if n == num:
        print('{}'.format(n), end = ' ')
    else:
        print('x {}'.format(num), end = ' ')
    num -= 1
print('= {}'.format(fat)) 
    