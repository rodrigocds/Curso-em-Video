from random import randint

pc = randint(0, 10)
tent = 1
player = int(input(""""Sou seu computador...
Acabei de pensar em número de 0 a 10.
Será que você consegue adivinhar qual foi?
Qual é o seu palpite? """))

while pc != player:
    tent += 1
    if pc < player:
        print('Menos... ', end = '')
    else:
        print('Mais... ', end = '')
    player = int(input('Tente Mais uma vez.\nQual é o seu palpite? '))

print('Acertou com {} tentativas. Parabéns!'.format(tent))