casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos ele vai pagar? '))
meses = anos * 12
prest = casa / meses
print('O valor da prestação será de R${:.2f}'.format(prest))
if prest > 30/100 * salario:
    print('SEU EMPRÉSTIMO FOI NEGADO!!')
    print('O valor da prestação mensal excede 30% do seu salário')
else:
    print('SEU EMPRÉSTIMO FOI ACEITO!!')
    print('O valor mensal da prestação da casa será de R${:.2f}'.format(prest))

