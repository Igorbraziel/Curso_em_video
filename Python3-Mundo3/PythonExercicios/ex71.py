numeros = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO',
           'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ',
           'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE',
           'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
    print('Tente novamente.', end = ' ')
print(f'Você digitou o número {numeros[num]}')