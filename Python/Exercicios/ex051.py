print('=' * 25)
print('10 TERMOS DE UMA PA')
print('=' * 25)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
formula = termo + (10 - 1) * razao

for c in range(termo, formula + razao, razao):
    print('{} > '.format(c), end = '')
print('ACABOU!')