print('-=-'*20)
print('analisador de triangulos')
print('-=-' *20  )
r1= float(input('primeiro segmento:'))
r2= float(input('segundo segmento:'))
r3= float(input('terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print(' os segmentos acima PODEM FORMAR triangulo!')
else: 
    print( 'os segmentos acima NÃO PODEM FORMAR triangulo\033[m')