from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

vit = 0
while True:
    player = int(input('Digite um valor: '))
    PlayerPI = ''
    playerPI = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    pc = randint(0, 10)

    num = player + pc
    if num % 2 == 0:
        ParImpar = 'P'
    else:
        ParImpar = 'I'
    print('=-' * 20)

    print(f'Você jogou {player} e o computador {pc}. TOTAL de {num} deu {ParImpar}.')
    if playerPI == ParImpar:
        print('Você VENCEU! Vamos jogar novamente...')
        vit += 1
    else:
        print('Você PERDEU!')
        break   
print('=-' * 20)
print(f'GAME OVER! Você venceu {vit} vezes.')