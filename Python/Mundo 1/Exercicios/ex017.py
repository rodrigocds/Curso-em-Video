from math import hypot

catO = float(input('Comprimento do cateto oposto: '))
catA = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}'.format(hypot(catO, catA)))

