dado = input('Digite algo: ')
print('{} é {}'.format(dado, type(dado)))
print('{} é {}: {}'.format(dado, 'numérico', dado.isnumeric()))
print('{} é {}: {}'.format(dado, 'alfa-numérico', dado.isalnum()))
print('{} é {}: {}'.format(dado, 'alfabético', dado.isalpha()))
print('{} esta {}: {}'.format(dado, 'em letras minusculas', dado.islower()))
print('{} esta {}: {}'.format(dado, 'em letras maiúsculas', dado.isupper()))
print('{} esta {}: {}'.format(dado, 'espaçado', dado.isspace()))