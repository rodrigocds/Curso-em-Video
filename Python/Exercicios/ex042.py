n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    if n1 == n2 == n3:
        triangulo = 'EQUILÁTERO'
    elif (n1 == n2 and n3 != n2) or (n2 == n3 and n3 != n1) or (n3 == n1 and n1 != n2):
        triangulo = 'ISÓSCELES'
    else: 
        triangulo = 'ESCALENO'
    print('Os segmentos acima PODEM FORMAR um triângulo {}'.format(triangulo))
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
