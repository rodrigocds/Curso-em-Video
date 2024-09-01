from datetime import date

trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - trabalhador['nascimento']
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
del(trabalhador['nascimento'])
if trabalhador['ctps'] == 0:
    for k, v in trabalhador.items():
        print(f' - {k} tem o valor {v}')
else:
    trabalhador['anoTrab'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['anoTrab'] + 35) - date.today().year)
    print('=' * 30)
    for k, v in trabalhador.items():
        print(f'- {k} tem o valor {v}')
