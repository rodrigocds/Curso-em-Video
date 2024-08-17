peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / altura ** 2

if imc < 18.5:
    status = 'Abaixo do Peso normal'
elif imc <= 25:
    status = 'Peso Ideal'
elif imc <= 30:
    status = 'Sobrepeso'
elif imc <= 40:
    status = 'OBESIDADE'
else:
    status = 'OBESIDADE MÓRBIDA, cuidado'

print('O IMC dessa pessoa é de {:.2f}\nVocê está em {}!'.format(imc, status))