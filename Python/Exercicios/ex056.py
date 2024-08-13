totIdade = 0
mHomem = 0
mNome = ''
mMulher = 0

for c in range (1, 5):
    print('--- {}ª PESSOA ---'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().upper())

    totIdade += idade

    if sexo == 'M':
        if idade > mHomem:
            mHomem = idade
            mNome = nome

    if sexo == 'F' and idade < 20:
        mMulher += 1

MedIdade = totIdade / 4

print('A média idade do grupo é de {:.1f} anos'.format(MedIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(mHomem, mNome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mMulher))