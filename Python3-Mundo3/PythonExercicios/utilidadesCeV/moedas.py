def dobro(num, op = False):
    num *= 2
    if op:
        return moeda(num)
    return num


def metade(num, op = False):
    num /= 2 
    if op:
        return moeda(num)
    return num


def aumentar(num, taxa = 0, op = False):
    num = num + (num * taxa / 100)
    if op:
        return moeda(num)
    return num


def diminuir(num, taxa = 0, op = False):
    num = num - (num * taxa / 100)
    if op:
        return moeda(num)
    return num


def moeda(num):
    reais = f'R${num:.2f}'.replace('.', ',')
    return reais


def resumo(num, aum = 0, dim = 0):
    print('=' * 40)
    print(f'{"RESUMO TOTAL":^40}')
    print('=' * 40)
    print('Preço analisado: ', f'{moeda(num):<10}')
    print('Dobro do preço : ', f'{moeda(dobro(num)):<10}')
    print('Metade do preço: ', f'{moeda(metade(num)):<10}')
    print(f'aumento de {aum}% : ', f'{moeda(aumentar(num, aum)):<9}')
    print(f'desconto de {dim}%: ', f'{moeda(diminuir(num, dim)):<10}')
    print('=' * 40)