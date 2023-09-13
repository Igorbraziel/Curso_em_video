from datetime import date
dados = dict()
dados['nome'] = str(input('Digite o seu nome: '))
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Número da carteira de trabalho (0 caso não tenha): '))
dados['Idade'] = date.today().year - dados['nascimento']
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Digite o seu salário: '))
    dados['Aposentadoria'] = (35 - (date.today().year - dados['contratação']) + dados['Idade'])
    print(dados)
    for k in dados.keys():
        print(f'{k} tem o valor {dados[k]}')
else:
    print(dados)
    for k in dados.keys():
        print(f'{k} tem o valor {dados[k]}')
