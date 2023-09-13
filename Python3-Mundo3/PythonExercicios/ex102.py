def fatorial(num, show = False):
    """
    Calcula o fatorial de um número
    """
    fat = 1
    if show == False:
        while num > 0:
            fat *= num
            num -= 1
    elif show == True:
        while num > 0:
            if num > 1:
                print(f'{num} x ', end = '')
            else:
                print(f'{num} = ', end = '')
            fat *= num
            num -= 1
    print(fat)    


n = int(input('Digite um número para ver seu fatorial: '))
op = str(input('Deseja ver o calculo do fatorial aparecendo? [S/N]: ')).upper().strip()[0]
while op not in 'SN':
    print('Opção inválida!')
    op = str(input('Deseja ver o calculo do fatorial aparecendo? [S/N]: ')).upper().strip()[0]

if op == 'S':
    fatorial(n, True)
else:
    fatorial(n)
    