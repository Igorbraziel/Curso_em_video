salario = float(input('Digite o seu salário: R$'))

if salario > 1250:
    print('Seu salário com aumento é de R${:.2f}'.format(110/100*salario))
else:
    print('Seu salário com aumento é de R${:.2f}'.format(115/100*salario))