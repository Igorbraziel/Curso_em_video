from random import randint
print('≃' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('≃' * 30)
k = 0
while True:
    comp = randint(0, 10)
    jog = int(input('Digite um valor: '))
    op = str(input('Você quer par ou ímpar? [P/I]: ')).strip().upper()[0]
    while op not in 'PpIi':
        op = str(input('Você quer par ou ímpar? [P/I]: ')).strip().upper()[0]
    soma = comp + jog
    if soma % 2 == 0 and op in 'Pp':
        print('≃' * 40)
        print('Você venceu!')
        print(f'Eu joguei {comp} e você jogou {jog}, E {soma} É PAR')
        print('≃' * 40)
        k += 1
    elif soma % 2 != 0 and op in 'Pp':
        print('≃' * 40)
        print('Você perdeu!')
        print(f'Eu joguei {comp} e você jogou {jog}, E {soma} É ÍMPAR')
        print('≃' * 40)
        break
    elif soma % 2 == 0 and op in 'Ii':
        print('≃' * 40)
        print('Você perdeu!')
        print(f'Eu joguei {comp} e você jogou {jog}, E {soma} É PAR')
        print('≃' * 40)
        break
    elif soma % 2 != 0 and op in 'Ii':
        print('≃' * 40)
        print('Você venceu!')
        print(f'Eu joguei {comp} e você jogou {jog}, E {soma} É ÍMPAR')
        print('≃' * 40)
        k += 1
    print('Vamos jogar de novo, você venceu dessa vez!')
print('≃' * 30)
print(f'GAME OVER, VOCÊ VENCEU {k} VEZES')
print('≃' * 30)