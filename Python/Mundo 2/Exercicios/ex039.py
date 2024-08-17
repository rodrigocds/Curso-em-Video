from datetime import date

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, date.today().year))

if idade < 18:
    dif = 18 - idade
    anoAlistamento = date.today().year + dif
    print('Ainda faltam {} anos para o alistamento.\nSeu alistamento será em {}.'.format(dif, anoAlistamento))
elif idade > 18:
    dif = idade - 18
    anoAlistamento = date.today().year - dif
    print('Você deveria ter se alistado há {} anos\nSeu alistamento foi em {}'.format(dif, anoAlistamento))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')