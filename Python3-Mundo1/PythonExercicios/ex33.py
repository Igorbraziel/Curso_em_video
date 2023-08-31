n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 >= n2:
    if n1 >= n3:
        if n3 >= n2:
            print('O maior número é {:.2f} e o menor é {:.2f}'.format(n1, n2))
        else:
            print('O maior número é {:.2f} e o menor é {:.2f}'.format(n1, n3))
    else:
        print('O maior número é {:.2f} e o menor é {:.2f}'.format(n3, n2))
if n2 >= n1:
    if n2 >= n3:
        if n3 >= n1:
            print('O maior número é {:.2f} e o menor é {:.2f}'.format(n2, n1))
        else:
            print('O maior número é {:.2f} e o menor é {:.2f}'.format(n2, n3))
    else:
        print('O maior número é {:.2f} e o menor é {:.2f}'.format(n3, n1))