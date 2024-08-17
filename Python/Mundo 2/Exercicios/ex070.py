print('-' * 25)
print('LOJA SUPER BARATÃO')
print('-' * 25)
tot = mil = barato =  c = 0 
prodBarato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))

    tot += preco

    if preco > 1000:
        mil += 1

    if c == 0 or preco < barato:
        barato = preco
        prodBarato = produto
        c += 1

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break
print('-' * 25)
print('FIM DO PROGRAMA')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prodBarato} que custa R${barato:.2f}')