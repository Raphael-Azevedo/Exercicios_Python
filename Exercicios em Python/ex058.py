from random import randint
from time import sleep
n1 = int(input('Digite um numero inteiro entre 0 a 10: '))
print('PROCESSANDO ...')
sleep(3)
n2 = randint(0, 10)
count = 1
while n1 != n2:
    n1 = int(input('Você errou tente novamente: '))
    count += 1
print('Você GANHOU!! o numero certo é {}, você tentou {} vezes'.format(n2, count))
