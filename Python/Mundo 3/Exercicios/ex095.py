time = []
jogador = {}
gols = []
totGol = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range (1, part + 1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['golsDict'] = gols.copy()
    for c in jogador['golsDict']:
        totGol += c
    jogador['total'] = totGol
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    totGol = 0
    while True:
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:<3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999) para parar '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! não existe jogador com o código {busca} ')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}:')
        for i, j in enumerate(time[busca]['golsDict']):
            print(f'Na partida {i+1} fez {j} gols')
    print('-' * 30)
print('<< VOLTE SEMPRE >>')