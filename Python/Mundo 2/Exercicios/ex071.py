print('=' * 20)
print('BANCO CEV')
print('=' * 20)

num = int(input('Que valor você quer sacar? R$'))

caixa = num
ced = 50
tot = 0
while True:
    if caixa >= ced:
        caixa -= ced
        tot += 1
    else:
        if tot > 0:
            print(f'Total de {tot} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if caixa == 0:
            break
print('=' * 30)
print(('Volte sempre ao BANCO CEV! Tenha um bom dia!'))