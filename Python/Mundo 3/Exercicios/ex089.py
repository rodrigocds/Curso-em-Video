aluno = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[1] + dados[2]) / 2)
    aluno.append(dados[:])
    dados.clear()
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-=' * 15)
print(f'{'No.':<4}{'Nome':<10}{'Média':>8}')
print('-=' * 15)
for pos, val in enumerate(aluno):
    print(f'{pos:<4}{val[0]:<10}{val[3]:>8.1f}')

while True:
    cod = int(input('Mostrar a nota de qual aluno? (999) interrompe: '))
    if cod == 999:
        break
    if cod <= len(aluno) - 1:
        print(f'Notas de {aluno[cod][0]} são {aluno[cod][1:3]}')
    print('-' * 30)
print('FINALIZANDO... \n<<< VOLTE SEMPRE >>>')