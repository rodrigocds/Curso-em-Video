n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
print('SUa média foi {:.1f}'.format(med))

if med >= 6:
    print('Sua média foi boa parabéns!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')