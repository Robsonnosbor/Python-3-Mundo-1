distancia = float(input('qual e a distancia da sua viagem?'))
print('você esta prestes a começar uma distancia de {}km'.format(distancia))
if distancia<= 200:
    preço = distancia * 0.45
else:
    preço = distancia * 0.45
print('e o preço da passagem sera de R${:.2f}'.format(preço))