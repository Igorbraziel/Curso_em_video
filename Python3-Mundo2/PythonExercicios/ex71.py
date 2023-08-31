cores = {'verde': '\033[1;32m',
         'azul': '\033[4;34m',
         'magenta': '\033[1;35m',
         'limpa': '\033[m'}

print(f'{cores["magenta"]}:=:{cores["limpa"]}' * 6)
print(f'{cores["verde"]}BANCO DO ZÉ IGÃO{cores["limpa"]}')
print(f'{cores["magenta"]}:=:{cores["limpa"]}' * 6)

total = int(input('Qual será o valor sacado?\nR$'))

cin = vin = dez = um = qtd = 0

while total > 0:
    if total >= 50:
        cin = total // 50
        total = total - (50 * cin)
    elif total >= 20:
        vin = total // 20
        total = total - (20 * vin)
    elif total >= 10:
        dez = total // 10
        total = total - (10 * dez)
    elif total >= 1:
        um = total // 1
        total = total - (1 * um)

print()
print(f'{cores["verde"]}-{cores["limpa"]}' * 45)
print(f'{cores["azul"]}OBRIGADO POR TRABALHAR CONOSCO, VOLTE SEMPRE{cores["limpa"]}')
print(f'{cores["verde"]}-{cores["limpa"]}' * 45)
print()

if cin > 0:
    print(f'{cores["magenta"]}Notas de R$50: {cin}{cores["limpa"]}')
if  vin > 0:
    print(f'{cores["magenta"]}Notas de R$20: {vin}{cores["limpa"]}')
if dez > 0:
    print(f'{cores["magenta"]}Notas de R$10: {dez}{cores["limpa"]}')
if um > 0:
    print(f'{cores["magenta"]}Notas de R$1: {um}{cores["limpa"]}')
