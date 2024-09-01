from operator import itemgetter
from random import randint
from time import sleep


print('Valores sorteados: ')
jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking = []

for k, v in jogadores.items():
    print(f'{k} tirou o dado {v}.')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('== RANKING DOS JOGADORES ==')
for i, v in enumerate (ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)