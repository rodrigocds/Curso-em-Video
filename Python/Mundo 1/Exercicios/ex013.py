sal = float(input('Qual o salário de um funcionário? R$'))
novSal = sal + (sal * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, novSal))