from random import randint
from time import sleep
computador= randint(0,5)#faz o cumputador "pensar"
print('-=-'*20)
print('vou pensar em um numero entre 0 e 5. tente advinhar...')
print('-=-'*20)
jogador=int(input('em que numero eu pensei?'))#jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS! Você conseguiu vencer!')
else:
    print('GANHEI!Eu pensei no numero {} e nao no {} !'.format(computador , jogador))