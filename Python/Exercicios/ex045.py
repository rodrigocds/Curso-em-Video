import random, time

player = int(input("""Suas Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada? """))

pc = random.randint(0, 2)

time.sleep(1.5)
print('-=' * 15)
print('JO')
time.sleep(1.5)
print('KEN')
time.sleep(1.5)
print('PO!!!')
print('-=' * 15)
time.sleep(1.25)

if player == 0:
    print('Jogador jogou PEDRA')
elif player == 1:
    print('Jogador jogou PAPEL')
else:
    print('Jogador jogou TESOURA')

if pc == 0:
    print('Computador jogou PEDRA')
elif pc == 1:
    print('Computador jogou PAPEL')
else:
    print('Computador jogou TESOURA')

if player == pc:
    print('EMPATOU')
elif (player == 0 and pc == 2) or (player == 1 and pc == 0) or (player == 2 and pc == 1):
    print('JOGADOR VENCEU')
else:
    print('COMPUTADOR VENCEU')