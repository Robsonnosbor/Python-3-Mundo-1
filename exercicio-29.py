from re import A


velocidade = float(input('qual é a velocidade atual do carro?'))
if velocidade>80:
    print('MULTADO! VocÊ excedeu o limite permitido que é de 80km/hr')
    multa = (velocidade-80) * 7
    print('voce deve pagar uma multa de R${:.2f}'.format(multa))
    print('tenha um bom dia! dirija com segurança')