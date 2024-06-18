met = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(met, met / 1000, met / 100, met / 10, met * 10, met * 100, met* 1000))
