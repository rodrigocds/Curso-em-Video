nome = input('Qual é o seu nome? ')
if nome == 'Rodrigo':
    print('Que nome bonito!')
elif nome == 'Julia' or nome == 'Sara':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))