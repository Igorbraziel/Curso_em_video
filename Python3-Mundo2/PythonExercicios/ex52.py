n = int(input('Digite um número: '))
k = 0
dic = {'amarelo': '\033[1;33m',
       'vermelho': '\033[0;31m',
       'limpa': '\033[m'}
for i in range(1, n + 1):
    if n % i == 0:
        k += 1
        print('{}{}{}'.format(dic['amarelo'], i, dic['limpa']), end = ' ')
    else:
        print('{}{}{}'.format(dic['vermelho'], i, dic['limpa']), end = ' ')
print()
if k == 2:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))