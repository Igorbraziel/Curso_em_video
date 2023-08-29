import datetime

ano_atual = datetime.date.today().year

ano = int(input('Em que ano você nasceu? '))

dif = ano_atual - ano

print('Você tem {} anos'.format(dif))

if dif < 18:
    print('Falta {} anos para você se alistar'.format(18 - dif))
    print('Você deverá se alistar em {}'.format(ano + 18))
elif dif > 18:
    print('Você deveria ter se alistado {} anos atrás'.format(dif - 18))
    print('Você deveria ter se alistado em {}'.format(ano + 18))
else:
    print('Está na hora de você se alistar no serviço militar!!')
    print('Estamos em {}'.format(ano + 18))

