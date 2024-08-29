lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(num)
        lista.sort()
        print('Valor adicionado com sucesso...')
    escolha = ' '
    if escolha not in 'SsNn':
        escolha = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if escolha == 'N':
        break
print('=' * 30)
print(f'Você digitou os valores {lista}')
    
