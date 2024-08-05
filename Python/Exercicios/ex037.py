num = int(input('Digite um número inteiro: '))
bas = int(input("""Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL
Sua opção: """))

if bas == 1:
    opi = 'BINÁRIO'
    res = bin(num)
elif bas == 2:
    opi = 'OCTAL'
    res = oct(num)
elif bas == 3:
    opi = 'HEXADECIMAL'
    res = hex(num)
else:
    print('Opção inválida. Tente novamente.')


print('{} convertido para {} é igual a {}'.format(num, opi, res[2:]))
