print('Gerador de PA')
print('=-' * 20)

num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))

c = 10
res = num

while c > 0:
    print(f'{res} > ', end='')
    res += raz
    c -= 1
print('FIM')