from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1   
    print('=' * 60)
    print(f'Contagem de {inicio} até {fim} pulando de {passo} em {passo}:', end = ' ')
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end = ' ', flush = True)
            sleep(0.5)
    else:
        for c in range(inicio, fim - 1, -1 *(passo)):
            print(c, end = ' ', flush = True)
            sleep(0.5)
    print()
    print('=' * 60)


contador(1, 10, 1)
contador(10, 0, 2)
init = int(input('Digite o início da contagem: '))
final = int(input('Digite o fim da contagem: '))
cont = int(input('Digite o passo da contagem: '))
contador(init, final, cont)