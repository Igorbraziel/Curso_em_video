c = ''
while c != 'M' and  c != 'F':
    c = str(input('Digite o seu sexo: [M/F]: ')).upper()
    if c != 'M' and c != 'F':
        print('Opção inválida, tente novamente!')   
if c == 'M':
    print('Você é macho')
elif c == 'F':
    print('Você é fêmea')