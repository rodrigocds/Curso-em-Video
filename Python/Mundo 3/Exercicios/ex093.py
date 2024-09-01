jogador = {}
gols = []
totGol = 0
jogador['nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range (1, part + 1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['golsDict'] = gols.copy()
for c in jogador['golsDict']:
    totGol += c
jogador['total'] = totGol
print('=' * 30)
print(jogador)
print('=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 30)
print(f'O jogador {jogador["nome"]} jogou {part} partidas.')
for i, c in enumerate(gols):
    print(f'> Na partida {i + 1}, fez {c} gols.')
print(f'Foi um total de {jogador["total"]} gols')