velocidade = int(input('Digite a velocidade do seu carro em KM/H: '))

if velocidade > 80:
    print('Você excedeu o limite de velocidade de 80KM/H\nVocê foi multado em um valor de R$ {:.2f}'.format((velocidade - 80) * 7))
print('Tenha um bom dia, dirija com segurança!')    