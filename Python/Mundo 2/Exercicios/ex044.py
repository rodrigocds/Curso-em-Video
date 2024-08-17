preco = float(input('Preço das compras: R$'))
pagamento = int(input("""FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é a opção? """))

if pagamento == 1:
    porcentagem = (preco * 10) / 100
    precoFinal= preco - porcentagem
elif pagamento == 2:
    porcentagem = (preco * 5) /100
    precoFinal = preco - porcentagem
elif pagamento == 3:
    precoFinal = preco
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(preco / 2))
elif pagamento == 4:
    parcela = int(input('Quantas parcelas? '))
    precoFinal = preco + ((preco * 20) / 100)
    valorDiv = precoFinal / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, valorDiv))
else:
    precoFinal = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, precoFinal))