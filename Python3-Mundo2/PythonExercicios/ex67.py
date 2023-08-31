while True:
    num = int(input('Digite um número e veja a sua tabuada: '))
    if num < 0:
        break
    print(f'TABUADA DO {num:=^11}')
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
print()
print('PROGRAMA ENCERRADO')