n = int(input('Digite quantos números da sequência de fibonacci você quer ver: '))
n1 = 0
n2 = 1
n3 = 1

if n > 2:
    print('0 -> 1 ->', end = ' ')
elif n == 2:
    print('0 -> 1', end = '')
elif n == 1:
    print('0', end = '')
while n > 2:
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    if n == 3:
        print('{}'.format(n3))
    else:
        print('{} ->'.format(n3), end = ' ')
    n -= 1

