from random import randrange
from time import sleep
n1 = int(input('Digite um numero inteiro entre 0 a 5: '))
print('PROCESSANDO ...')
sleep(3)
n2 = randrange(4)
if n1 == n2:
    print('Parabens você venceu!')
else:
    print('Você errou o numero certo era {}'.format(n2))

