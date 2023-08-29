n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Você foi reprovado, estude mais!')
elif media >= 5 and media <= 6.9:
    print('Você ficou de recuperação')
elif media >= 7.0:
    print('Você foi aprovado, parabéns!')
print('Sua média foi {:.2f}'.format(media))