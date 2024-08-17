from datetime import date

nasc = int(input('Ano de Nascimento: '))

ano = date.today().year
idade = ano - nasc

if idade <= 9:
    modalidade = 'MIRIM'
elif idade <= 14:
    modalidade = 'INFANTIL'
elif idade <= 19:
    modalidade = 'JÚNIOR'
elif idade <= 25:
    modalidade = 'SÊNIOR'
else:
    modalidade = 'MASTER'
print('O atleta tem {} anos.\nClassificação: {}'.format(idade, modalidade))