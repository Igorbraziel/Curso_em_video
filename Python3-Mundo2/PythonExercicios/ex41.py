from datetime import datetime

ano_nasc = int(input('Digite em que ano você nasceu: '))

ano_atual = datetime.now().year

dic = {'azulEroxo': '\033[4;34;45m',
        'limpa': '\033[m'}

idade = ano_atual - ano_nasc

print('Você tem {} anos'.format(idade))

if idade >= 0 and idade <= 9:
    print('Sua categoria é {}MIRIM{}'.format(dic['azulEroxo'], dic['limpa']))
elif idade > 9 and idade <= 14:
    print('Sua categoria é {}INFANTIL{}'.format(dic['azulEroxo'], dic['limpa']))
elif idade > 14 and idade <= 19:
    print('Sua categoria é {}JUNIOR{}'.format(dic['azulEroxo'], dic['limpa']))
elif idade > 19 and idade <= 20:
    print('Sua categoria é {}SÊNIOR{}'.format(dic['azulEroxo'], dic['limpa']))
elif idade > 20:
    print('Sua categoria é {}MASTER{}'.format(dic['azulEroxo'], dic['limpa']))