from time import sleep
cores = {'Azul': '\033[1;44m',
         'Amarelo': '\033[1;43m',
         'Verde': '\033[1;42m',
         'limpa': '\033[m'}


def escreva(msg, cor, limpa):
    tam = len(msg) + 4
    print(f'{cor}~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(f'{limpa}')


def ajuda(função):
    escreva(f'Acessando o manual do comando ({função})...', cores['Amarelo'], cores['limpa'])
    escreva(help(função), cores['Azul'], cores['limpa'])


escreva('SISTEMA DE AJUDA PyHELP', cores['Verde'], cores['limpa'])

while True:
    m = str(input('Função ou Biblioteca > ')).strip()
    if m.upper == 'FIM':
        break
    ajuda(m) 

escreva('ESPERO TER AJUDADO, VOLTE SEMPRE...', cores['Verde'], cores['limpa'])

