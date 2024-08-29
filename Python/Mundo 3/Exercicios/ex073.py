clubes = 'Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Bahia', 'São Paulo', 'Cruzeiro', 'Atlético-MG', 'Athletico-PR', 'Vasco', 'Juventude', 'RB Bragantino', 'Internacional', 'Criciúma', 'Grêmio', 'Vitória', 'Corinthians', 'Fluminense', 'Cuiabá', 'Atlético-GO'

print(f'Lista de time do Brasileirão: {clubes}')
print('=' * 30)
print(f'Os 5 primeiros são: {clubes[0:5]}')
print('=' * 30)
print(f'Os 4 últimos são: {clubes[-4:]}')
print('=' * 30)
print(f'Times em ordem alfabética: {sorted(clubes)}')
print('=' * 30)
print(f'O Criciúma está na {clubes.index('Criciúma') + 1}° posição.')