from math import factorial


num = int(input('Digite um número para calcular o seu fatorial: '))
print(f'Calculando {num}!: ', end='')
contador = num
while contador > 0:
    print(f'{contador} ', end='')
    print('x ' if contador > 1 else '= ', end='')
    contador -= 1
    if contador == 0:
        print(f'{factorial(num)}')