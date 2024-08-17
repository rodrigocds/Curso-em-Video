print('-=' * 20)
print('Sequência de Fibonacci')
print('-=' * 20)

qtd = int(input('Quantos termos você quer mostrar? '))

n1 = 0
n2 = 1
print(f'{n1} > {n2} > ',end='')
c = 3
while c <= qtd:
    n3 = n1 + n2
    print(f'{n3} > ', end='')
    n1 = n2
    n2 = n3
    c += 1
print('FIM')