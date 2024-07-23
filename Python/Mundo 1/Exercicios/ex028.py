from random import randint
from time import sleep

num = int(input('Vou pensar em um número entre 0 e 5. Tente adivinhar... \nEm que número pensei? '))

print('PROCESSANDO...')
sleep(3)
numCop = randint(0, 5)

if num != numCop:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(numCop, num))
else:
    print('PARABÉNS! Você conseguiu me vencer!')

print(numCop)