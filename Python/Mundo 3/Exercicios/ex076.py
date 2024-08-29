print('-' * 30)
print('LISTAGEM DE PREÇOS')
print('-' * 30)

tupla = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90

for c in tupla:
    if isinstance(c, float):
        print(f'R$ {c:>1.2f}\n')
    else:
        print(f'{c:.<30}', end='')
    
print('-' * 30)

