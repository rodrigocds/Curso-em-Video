num = int(input('Digite um número [999] para parar: '))
qtd = tot = 0

while num != 999:
    qtd += 1
    tot += num
    num = int(input('Digite um número [999] para parar: '))
print(f'Você digitou {qtd} números e a soma entre eles foi {tot}')
