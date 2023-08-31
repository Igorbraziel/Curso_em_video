total = qtdProd = nomeBarato = precoBarato = 0
while True:
    produto = str(input('Digite o nome do produto a ser compro: ')).strip().upper()
    preco = float(input('Digite o preço do produto em R$: '))
    if total == 0:
        nomeBarato = produto
        precoBarato = preco
    total += preco
    if preco > 1000:
        qtdProd += 1
    if preco < precoBarato:
        nomeBarato = produto
        precoBarato = preco
    opção = str(input('Você deseja continuar a inserir dados? [S/N]: ')).strip().upper()[0]
    while opção not in 'Ss' and opção not in 'Nn':
        print('RESPOSTA INVÁLIDA, INSIRA OS DADOS NOVAMENTE')
        opção = str(input('Você deseja continuar a inserir dados? [S/N]: ')).strip().upper()[0]
    if opção in 'Nn':
        break
print(f'O total gasto na compra é de R${total:.2f}')
print(f'Houveram {qtdProd} produtos que custaram mais de R$1000')
print(f'O produto mais barato foi {nomeBarato} e o seu preço foi R${precoBarato:.2f}')
    