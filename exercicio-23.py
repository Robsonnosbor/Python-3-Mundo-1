from re import M, U
from socketserver import UDPServer


num = int(input( 'Informe o numero:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10 
m = num // 1000 % 10
print (' Analisando o número {}' .format(num))
print ('Unidade:{}'. format (u))
print ('dezena:{}' .format(d))
print ('Centena:{}'.format(c))
print ('Milhar {}' .format (m ))
