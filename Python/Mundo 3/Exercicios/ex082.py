par = []
impar = []
todos = []

while True:
    num = int(input('Digite um número: '))
    todos.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if escolha == 'N':
        break

print(f'A lista completa é {todos}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
    