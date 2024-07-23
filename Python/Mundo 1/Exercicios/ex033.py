n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

ordem = [n1, n2, n3]
ordem.sort()

print('O menor valor digitado foi {}'.format(ordem[0]))
print('O maior valor digitado foi {}'.format(ordem[-1]))