from random import randint
from time import sleep

mega = []
lista = []

print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)

qtd = int(input('Quantos jogos você quer que eu sorteie? '))

print('-=' * 3, f' SORTEANDO {qtd} JOGOS ', '-=' * 3)
for c in range (0, qtd):
    for d in range(1, 7):
        num = randint(0, 60)
        while num not in lista:
            lista.append(num)
            lista.sort()
    mega.append(lista[:])
    lista.clear()
    print(f'Jogo {c + 1}: {mega[c]}')
    sleep(1.5)
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
