mais18 = homem = m20 = 0 
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print(('-' * 20))

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        m20 += 1

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continua == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {m20} mulheres com menos de 20 anos')