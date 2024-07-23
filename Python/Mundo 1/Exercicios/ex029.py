vel = int(input('Qual a velocidade atual do carro? '))

if vel > 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = float((vel - 80) * 7)
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${:.2f}!'.format(multa))