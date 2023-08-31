from random import randint
from time import sleep

dic = {'azulEcinza': '\033[1;34;47m',
       'vermelho': '\033[1;31m',
       'limpa': '\033[m',
       'cianoEroxo': '\033[1;36;45m'}
    
dic2 = {'1': 'PEDRA',
        '2': 'PAPEL',
        '3': 'TESOURA'}

comp = randint(1, 3)

print('=~' * 20)
print('VAMOS JOGAR {}JOKENPÔ{}'.format(dic['vermelho'], dic['limpa']))
print('~=' * 20)
sleep(2)

print('Digite {}1{} para {}PEDRA{}'.format(dic['cianoEroxo'], dic['limpa'], dic['cianoEroxo'], dic['limpa']))
print('Digite {}2{} para {}PAPEL{}'.format(dic['cianoEroxo'], dic['limpa'], dic['cianoEroxo'], dic['limpa']))
print('Digite {}3{} para {}TESOURA{}'.format(dic['cianoEroxo'], dic['limpa'], dic['cianoEroxo'], dic['limpa']))
print()
sleep(2)

n = int(input('Digite qual é a sua escolha: '))

print('{}PROCESSANDO...{}'.format(dic['azulEcinza'], dic['limpa']))
print()
sleep(3)

if n == comp:
    print('{}EMPATE{}'.format(dic['vermelho'], dic['limpa']))
    print('{}nós dois escolhemos {}{}'.format(dic['azulEcinza'], dic2[str(n)], dic['limpa']))
elif n == 1 and comp == 2:
    print('{}VOCÊ PERDEU!!!{}'.format(dic['vermelho'], dic['limpa']))
    print('{}Eu escolhi {} e você escolheu {}{}'.format(dic['cianoEroxo'], dic2[str(comp)], dic2[str(n)], dic['limpa']))
elif n == 1 and comp == 3:
    print('{}VOCÊ VENCEU!!!{}'.format(dic['vermelho'], dic['limpa']))
    print('{}Eu escolhi {} e você escolheu {}{}'.format(dic['cianoEroxo'], dic2[str(comp)], dic2[str(n)], dic['limpa']))
elif n == 2 and comp == 1:
    print('{}VOCÊ VENCEU!!!{}'.format(dic['vermelho'], dic['limpa']))
    print('{}Eu escolhi {} e você escolheu {}{}'.format(dic['cianoEroxo'], dic2[str(comp)], dic2[str(n)], dic['limpa']))
elif n == 2 and comp == 3:
    print('{}VOCÊ PERDEU!!!{}'.format(dic['vermelho'], dic['limpa']))
    print('{}Eu escolhi {} e você escolheu {}{}'.format(dic['cianoEroxo'], dic2[str(comp)], dic2[str(n)], dic['limpa']))
elif n == 3 and comp == 1:
    print('{}VOCÊ PERDEU!!!{}'.format(dic['vermelho'], dic['limpa']))
    print('{}Eu escolhi {} e você escolheu {}{}'.format(dic['cianoEroxo'], dic2[str(comp)], dic2[str(n)], dic['limpa']))
elif n == 3 and comp == 2:
    print('{}VOCÊ VENCEU!!!{}'.format(dic['vermelho'], dic['limpa']))
    print('{}Eu escolhi {} e você escolheu {}{}'.format(dic['cianoEroxo'], dic2[str(comp)], dic2[str(n)], dic['limpa']))


