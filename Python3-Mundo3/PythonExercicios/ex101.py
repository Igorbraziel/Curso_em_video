from datetime import date

    
def voto(ano):
    global idade
    idade = date.today().year - ano
    if 0 <= idade < 16:
        return 'NÃO VOTA'
    elif 16 <= idade < 18:
        return 'VOTO OPCIONAL'
    elif 18 <= idade <= 65:
        return 'VOTO OBRIGATÓRIO'
    elif 65 < idade:
        return 'VOTO OPCIONAL'


idade = 0
ano_nasc = int(input('Digite o seu ano de nascimento: '))
frase = voto(ano_nasc)
print(f'Com {idade} anos: {frase}')