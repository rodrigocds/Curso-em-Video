expressao = str(input('Digite a expressão: '))
frase = []
for c in expressao:
    if c == '(':
        frase.append('(')
    elif c == ')':
        if len(frase) > 0:
            frase.pop()
        else:
            frase.append(')')
            break


if len(frase) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')