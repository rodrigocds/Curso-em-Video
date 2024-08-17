sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    print('Dados inválidos. Por favor, ', end = '')
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
