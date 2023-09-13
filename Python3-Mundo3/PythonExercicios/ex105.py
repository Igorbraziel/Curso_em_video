def notas(*provas, sit = False):
    maior = menor = media = 0
    boletim = dict()
    for i, n in enumerate(provas):
        if i == 0 or n > maior:
            maior = n
        if i == 0 or n < menor:
            menor = n
        media += n
    media /= len(provas)
    boletim['Total'] = len(provas)
    boletim['Maior'] = maior
    boletim['Menor'] = menor
    boletim['Média'] = media
    if sit == True:
        if 7 <= boletim['Média'] <= 10:
            boletim['Situação'] = 'BOA'
        elif 6 <= boletim['Média'] < 7:
            boletim['Situação'] = 'RAZOÁVEL'
        elif 0 <= boletim['Média'] < 6:
            boletim['Situação'] = 'RUIM'
    return boletim

resp = notas(5.5, 2.5, 9, 8.5, sit = True)
print(resp)