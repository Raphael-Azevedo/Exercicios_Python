from random import randint
from time import sleep

palpites = list()
print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
x = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=' * 3, ' SORTEANDO', x, 'JOGOS ', '-=' * 3)
for c in range(0, x):
    linha = []
    for y in range(0, 6):
        i = (randint(0, 60))
        while i in linha:
            i = (randint(0, 60))
        linha.append(i)
    palpites.append(linha[:])
    linha.clear()
    sleep(1)
    print(f'Jogo {c + 1}: {sorted(palpites[c])}')

print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
