dic = dict()
dic['nome'] = str(input('Digite o seu nome: '))
dic['media'] = float(input(f'Digite a média do {dic["nome"]}: '))
if dic['media'] >= 7:
    dic['sit'] = 'APROVADO'
elif 5 <= dic['media'] < 7:
    dic['sit'] = 'RECUPERAÇÃO'
elif 0 <= dic['media'] < 5:
    dic['sit'] = 'REPROVADO'
print(dic)