contIdade = contMu = contH = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'Mm' and sexo not in 'Ff':
        sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        contIdade += 1
    if sexo in 'Mm':
        contH += 1
    if idade < 20 and sexo in 'Ff':
        contMu += 1
    opção = str(input('Deseja continuar a inserir dados? [S/N]: ')).upper().strip()[0]
    while opção not in 'Nn' and opção not in 'Ss':
        opção = str(input('Deseja continuar a inserir dados? [S/N]: ')).upper().strip()[0]
    if opção in 'Nn':
        break
print(f'Há {contIdade} pessoas com mais de 18 anos')
print(f'{contH} Homens foram cadastrados')
print(f'Há {contMu} mulheres cadastradas com menos de 20 anos')