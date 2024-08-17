from datetime import date
ano = date.today().year
maior = 0
menor = 0

for c in range (1, 8):
    pessoa = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = ano - pessoa
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} pessoas menores de idade'.format(maior, menor))