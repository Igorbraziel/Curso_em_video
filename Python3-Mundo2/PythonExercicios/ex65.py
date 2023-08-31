c = ''
media = 0
maior = 0
menor = 0
k = 0
while c != 'N':
    n = int(input('Digite um número: '))
    if c == '':
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n    
    media += n
    k += 1
    c = str(input('Deseja continuar? [S/N]:\n')).strip().upper()
media = media / k
print('Foram lidos {} valores'.format(k))
print('O maior valor lido é {}'.format(maior))
print('O menor valor lido é {}'.format(menor))
print('A média entre todos os valores lidos é {}'.format(media))