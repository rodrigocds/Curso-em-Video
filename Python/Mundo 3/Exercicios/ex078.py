lista = []
for c in range (0, 5):
    lista.append(int(input(f'Digite um número para a Posição {c}: ')))
print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ',end='')
for p, c in enumerate(lista):
    if c == max(lista):
        print(f'{p}... ',end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for p, c in enumerate(lista):
    if c == min(lista):
        print(f'{p}...', end='')