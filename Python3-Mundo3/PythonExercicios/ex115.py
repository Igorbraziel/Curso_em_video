from time import sleep

cores = {'verde': '\033[7;30;42m',
         'vermelho': '\033[7;30;41m',
         'limpa': '\033[m',
         'azul': '\033[7;30;44m',
         'ciano': '\033[7;30;46m'}

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO AO LER O ARQUIVO')
    else:
        print(a.read())

    
def leiaInt(frase):
    try:
        num = str(input(frase))
        return int(num)
    except KeyboardInterrupt:
        print('\033[7;37;41mO usuário não quis digitar esse valor!\033[m')
        return 0
    except:
        print('\033[7;37;41mERRO! DIGITE UM VALOR INTEIRO!\033[m')
        num = leiaInt(frase)
        return int(num)


def leiaFloat(frase):
    try:
        num = str(input(frase))
        return float(num)
    except KeyboardInterrupt:
        print('\033[7;37;41mO usuário não quis digitar esse valor!\033[m')
        return 0
    except:
        print('\033[7;37;41mERRO! DIGITE UM VALOR FLUTUANTE!\033[m')
        num = leiaFloat(frase)
        return float(num)
    
    
def escreveArquivo(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO NA ABERTURA DO ARQUIVO')
    else:
        a.write(f'{cores["azul"]}{nome:<20}{idade:>10} anos{cores["limpa"]}\n')


arq = 'cursoemvideo.txt'
while True:
    try:
        a = open(arq, 'rt')
        a.close()
        break
    except:
        arq = 'cursoemvideo.txt'

while True:
    print('=' * 50)
    print(f'{cores["ciano"]}{"MENU PRINCIPAL":^50}{cores["limpa"]}')
    print('=' * 50)
    print(f'{cores["verde"]}1{cores["limpa"]} - {cores["azul"]}Ver pessoas cadastradas{cores["limpa"]}')
    print(f'{cores["verde"]}2{cores["limpa"]} - {cores["azul"]}Cadastrar nova pessoa{cores["limpa"]}')
    print(f'{cores["verde"]}3{cores["limpa"]} - {cores["azul"]}Sair do sistema{cores["limpa"]}')
    print('=' * 50)
    while True:
        try:
            op = int(input(f'{cores["verde"]}Sua opção:{cores["limpa"]} '))
        except ValueError:
            print(f'\n{cores["vermelho"]}ERRO, DIGITE UMA OPÇÃO VÁLIDA!{cores["limpa"]}\n')
        else:
            if 1 <= op <= 3:
                break
            else:
                print(f'\n{cores["vermelho"]}ERRO, DIGITE UMA OPÇÃO VÁLIDA!{cores["limpa"]}\n')
    if op == 1:
        print('=' * 50)
        print(f'{cores["ciano"]}{f"PESSOAS CADASTRADAS":^50}{cores["limpa"]}')
        print('=' * 50)
        lerArquivo('cursoemvideo.txt')
    elif op == 2:
        print('=' * 50)
        print(f'{cores["ciano"]}{f"OPÇÃO {op}":^50}{cores["limpa"]}')
        print('=' * 50)
        nome = str(input('Digite o nome: '))
        idade = leiaInt('Idade: ')
        escreveArquivo(arq, nome, idade)
    elif op == 3:
        print('=' * 50)
        print(f'{cores["ciano"]}{f"SAINDO DO SISTEMA...":^50}{cores["limpa"]}')
        print('=' * 50)
        break
    sleep(2)