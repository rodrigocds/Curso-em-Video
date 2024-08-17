dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

val = float((dia * 60) + (km * 0.15))

print('O totaL a pagar é de R${:.2f}'.format(val))