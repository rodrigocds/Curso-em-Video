num = int(input('Digite um número: '))
primo = 0

for c in range(1, num + 1):
    if num % c == 0:
        primo += 1
    print(c, end = ' ')
print('\nO número {} foi divisível {} vezes'.format(num, primo))

if primo == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')