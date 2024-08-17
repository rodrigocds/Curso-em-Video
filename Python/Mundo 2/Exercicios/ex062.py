print('Gerador de PA')
print('=-' * 20)

num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))

c = 10
res = num
qtd = 10

while c > 0:
    print(f'{res} > ', end='')
    res += raz
    c -= 1

adc = int(input('PAUSA\nQuantos termos você quer mostrar a mais? '))
c = adc
while adc != 0:
    while c > 0:
        print(f'{res} > ', end='')
        res += raz
        c -= 1
        qtd += 1
    adc = int(input('PAUSA\nQuantos termos você quer mostrar a mais? '))
    c += adc
print(f'Progressão finalizada com {qtd} termos mostrados')