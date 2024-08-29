matriz = [[0, 0, 0,], [0, 0, 0], [0, 0, 0]]
par =  mLinha = tColuna = 0

for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l] [c]}]', end='')
    print()
print('=' * 30)
print(f'A soma dos valores pares é {par}')
for l in range (0,3):
    tColuna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {tColuna}')
for c in range (0,3):
    if c == 0:
        mLinha += matriz[1][c]
    else:
        if matriz[1][c] > mLinha:
            mLinha = matriz[1][c]
print(f'O maior valor da segunda linha é {mLinha}')