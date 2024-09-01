dados = {}
pessoas = []
mulheres = []
totIdade = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while dados['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    totIdade += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
    while escolha not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()
    if escolha == 'N':
        break
medIdade = totIdade / len(pessoas)
print('=' * 30)
print(f'A) Ao todo temos {len(pessoas)} cadastradas.')
print(f'B) A média de idade é de {medIdade:.2f}')
print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) Lista das pessoas que estão acima da média:')
for c in pessoas:
    if c['idade'] >= medIdade: 
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
print('\n<< ENCERRADO >>')