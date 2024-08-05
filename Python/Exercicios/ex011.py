#2m 1l
lag = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lag * alt
tinta = area / 2

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(lag, alt, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(tinta))