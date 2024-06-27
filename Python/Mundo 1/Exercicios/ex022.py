nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome... \nSeu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

nomeFor = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomeFor[0], len(nomeFor[0])))