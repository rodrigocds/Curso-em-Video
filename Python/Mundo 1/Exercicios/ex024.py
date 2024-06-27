cidade = str(input('Em que cidade você nasceu? ')).strip()
cidSan = cidade.split()
print('Santo' in cidSan[0].capitalize())