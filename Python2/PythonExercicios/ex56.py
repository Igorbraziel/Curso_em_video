listaN = []
listaI = []
listaS = []
mediaI = 0
maiorI = 0
indiceM = 0
k = 0
for i in range(0, 4):
    print('-' * 5, end = '')
    print('{}ā pessoa'.format(i + 1), end = '')
    print('-' * 5)
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu sexo (Homem ou Mulher): '))
    mediaI += idade
    listaN.append(nome)
    listaI.append(idade)
    listaS.append(sexo)
mediaI = mediaI / 4
for i in range(0, 4):
    if listaI[i] > maiorI and listaS[i].upper() == 'HOMEM':
        maiorI = listaI[i]
        indiceM = i
    if listaI[i] < 20 and listaS[i].upper() == 'MULHER':
        k += 1
print('A média de idades é de {} anos.'.format(mediaI))
print('O homem mais velho tem {} anos e se chama {}'.format(listaI[indiceM], listaN[indiceM]))
print('{} mulheres possuem menos de 20 anos'.format(k))
