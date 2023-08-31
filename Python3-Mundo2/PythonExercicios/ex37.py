num = int(input('Digite um número inteiro: '))

dic = {'azul': '\033[1;34m',
       'limpa' : '\033[m',
       'amarelo' : '\033[1;33m'}

print('Digite {}1{} para {}binário{}'.format(dic['azul'], dic['limpa'], dic['amarelo'], dic['limpa']))
print('Digite {}2{} para {}hexadecimal{}'.format(dic['azul'], dic['limpa'], dic['amarelo'], dic['limpa']))
print('Digite {}3{} para {}octal{}'.format(dic['azul'], dic['limpa'], dic['amarelo'], dic['limpa']))
 
c = int(input())

if c == 1:
    bin = int(bin(num)[2:])
    print('O número {} convertido para a base binária é {}'.format(num, bin))
elif c == 2:
    hex = hex(num)[2:]
    print('O número {} convertido para a base hexadecimal é {}'.format(num, hex))
elif c == 3:
    oct = int(oct(num)[2:])
    print('O número {} convertido para a base octal é {}'.format(num, oct))

