import random
from time import sleep
num = int(random.randint(0, 5))

print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5...')
print('-=-' * 10)
n = int(input('tente advinhar em que número eu pensei: '))
print('PROCESSANDO...')
sleep(3)
if n == num:
    print('VOCÊ VENCEU!, eu pensei no número {} e você também'.format(n))
else:
    print('VOCÊ PERDEU, eu pensei no número {} e você no {}'.format(num, n))