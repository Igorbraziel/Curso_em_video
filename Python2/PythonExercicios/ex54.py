from datetime import date
ano_atual = date.today().year
soma = 0
k = 0
for i in range(0, 7):
    ano = int(input('Digite o {}º ano de nascimento: '.format(i + 1)))
    if ano_atual - ano >= 21:
        k += 1
print('{} pessoas são maiores de idade'.format(k))
print('{} pessoas não são maiores de idade'.format(7 - k))