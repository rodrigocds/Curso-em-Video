print('Digite 6 números: ')
soma = 0
par = 0
for c in range (1, 7):
    num = int(input())
    if num % 2 == 0:
        soma += num
        par += 1
print('Temos {} números pares e a soma deles é {}'.format(par, soma))
