pessoas = []
dados = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('=' * 30)
    
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai:.2f}Kg. Peso de ',end='')

for c in pessoas:
    if c[1] == mai:
        print(f'{c[0]} ',end='')

print(f'\nO menor peso foi de {men:.2f}Kg. Peso de ',end='')
for c in pessoas:
    if c[1] == men:
        print(f'{c[0]} ',end='')
