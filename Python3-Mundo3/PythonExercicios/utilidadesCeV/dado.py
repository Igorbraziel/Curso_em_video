def leiaDinheiro(frase):
    num = str(input(frase)).replace(',', '.').strip()
    if num.isalpha() or num == '':
        print(f'\033[4;31mERRO! ("{num.upper()}") NÃO É UM NÚMERO VÁLIDO\033[m')
        num = leiaDinheiro(frase)
        return float(num)
    else:
        num = float(num)
        return num        
