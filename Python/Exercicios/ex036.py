cas = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
fin = int(input('Quantos anos de financiamento? '))

pre = cas / (fin * 12)
exe = (sal * 30) / 100

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(cas, fin, pre))

if pre >= exe:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
