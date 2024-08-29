palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'

for c in palavras:
    print(f'\nNa palavra {c} temos ', end= '')
    for d in c:
        if d in 'AEIOU':
                print(f'{d} ', end='')