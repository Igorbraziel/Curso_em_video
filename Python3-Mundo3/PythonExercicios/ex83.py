exp = str(input('Digite a sua expressão: '))
if exp.count('(') == exp.count(')') and exp.find('(') < exp.find(')'):
    print('Sua expressão é valida!')
else:
    print('Sua expressão é inválida!')