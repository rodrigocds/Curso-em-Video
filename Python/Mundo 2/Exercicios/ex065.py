continua = 's'
qtd = soma = 0
while continua == 's':
    num = int(input('Digite um número: '))
    if qtd == 0:
        maior = menor = num
    else: 
        if num > maior:
            aior = num
        if num < menor:
            menor = num
    qtd += 1
    soma += num
    continua = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
print(f'Você digitou {qtd} números e a média foi {soma / qtd:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')