peso= float (input('digite seu peso:'))
altura= float (input('digite sua altura:'))
imc= peso/ (altura ** 2)
print ('o imc dessa pessoa e {:.1f}' .format(imc))
if 18.5 <= imc < 25:
     print ('seu peso esta normal')
elif 25 <=imc < 30:
    print ('voce esta com sobrepeso')
elif 30<= imc < 40:
    print ('print voce esta com obesidade cuidado')
elif imc > 40:
    print('voce esta com obesidade grave, cuidado') 
    