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
    

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro foi {inteiro} e o valor real foi {real}')