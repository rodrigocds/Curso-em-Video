frase = str(input('Digite uma frase: ')).strip().upper()
div = frase.split()
junto = ''.join(div)
inverso = ''

for c in range (len(junto) - 1, -1, -1):
    inverso += junto[c]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
