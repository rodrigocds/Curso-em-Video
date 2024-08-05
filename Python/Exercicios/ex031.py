dis = int(input('Qual a distância da sua viagem? '))

print('Você está prestes a começar uma viagem de {}Km.'.format(dis))
preco = float(0)
if dis > 200:
    preco = dis * 0.45
else:
    preco = dis * 0.50
print('E o preço da sua passagem será de R${:.2f}'.format(preco))