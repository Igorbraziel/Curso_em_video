frase = input('Digite uma frase qualquer: ').strip()

print('o caractere "A" aparece {} vezes'.format(frase.upper().count('A')))

print('o caractere "A" aparece pela primeira vez na posição {}'.format(frase.upper().find('A')))

print('o caractere "A" aparece pela última vez na posição {}'.format(frase.upper().rfind('A')))