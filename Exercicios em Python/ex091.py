from time import sleep
from random import randint
from operator import itemgetter
dados = dict()
print('Valores sorteados:')
for c in range(0, 4):
    dados[f'jogador{c+1}'] = randint(1, 6)
for k, v in dados.items():
    print(f'O {k} tirou {v}')
    sleep(0.8)
print('Ranking dos jogadores: ')
for i, v in enumerate(sorted(dados.items(), key=itemgetter(1), reverse=True)):
    print(f'O {i+1}º Lugar : {v[0]} com {v[1]}')
    sleep(0.8)
