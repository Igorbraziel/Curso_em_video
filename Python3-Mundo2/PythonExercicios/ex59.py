cores = {'azul': '\033[1;34;40m',
         'verde': '\033[1;32;47m',
         'limpa': '\033[m'}
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
op = 0
while op != 5:    
    print('{}MENU{}'.format(cores['verde'], cores['limpa']))
    print('{}[1]{} {}SOMAR:{}'.format(cores['azul'], cores['limpa'], cores['verde'], cores['limpa']))
    print('{}[2]{} {}MULTIPLICAR:{}'.format(cores['azul'], cores['limpa'], cores['verde'], cores['limpa']))
    print('{}[3]{} {}MAIOR:{}'.format(cores['azul'], cores['limpa'], cores['verde'], cores['limpa']))
    print('{}[4]{} {}NOVOS NÚMEROS:{}'.format(cores['azul'], cores['limpa'], cores['verde'], cores['limpa']))
    print('{}[5]{} {}SAIR DO PPROGRAMA:{}'.format(cores['azul'], cores['limpa'], cores['verde'], cores['limpa']))
    op = int(input('Digite sua escolha: '))
    if op == 1:
        print('A soma entre {:.2f} e {:.2f} equivale a {:.2f}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicação entre {:.2f} e {:.2f} equivale a {:.2f}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('O maior valor entre {:.2f} e {:.2f} é {:.2f}'.format(n1, n2, n1))
        elif n2 > n1:
            print('O maior valor entre {:.2f} e {:.2f} é {:.2f}'.format(n1, n2, n2))
        else:
            print('Não existe maior valor, ambos os valores são iguais')
    elif op == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif op != 5: 
        print('OPÇÃO INVÁLIDA!!!')
print('{}PROGRAMA ENCERRADO{}'.format(cores['azul'], cores['limpa']))