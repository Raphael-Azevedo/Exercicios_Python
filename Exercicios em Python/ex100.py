from random import randint
from time import sleep
sorteio = list()


def sorti():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        sorteio.append(randint(0, 10))
        print(sorteio[c], end=' ')
        sleep(0.5)
    print('PRONTO!')


def somapar():
    soma = 0
    print(f'Somando os valores de {sorteio},', end = ' ')
    for i, v in enumerate(sorteio):
        if v % 2 == 0:
            soma += v
    print(f'temos {soma}')


sorti()
somapar()