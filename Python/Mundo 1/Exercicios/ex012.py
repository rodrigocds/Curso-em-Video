preco = float(input('Qual o preço do produto? R$'))
des = (preco * 5) / 100
precoNovo = preco - des

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, precoNovo))