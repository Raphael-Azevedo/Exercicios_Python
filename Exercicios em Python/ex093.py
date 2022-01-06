apro = dict()
gol = list()
apro['Nome'] = str(input('Nome do jogador: '))
partida = int(input(f'Quantas partidas {apro["Nome"]} jogou: '))
for c in range(0, partida):
    gol.append(int(input(f'Quantos gols na partida {c}? ')))
apro['Gols'] = gol[:]
apro['Total'] = sum(gol)
print('-='*40)
print(apro)
print('-='*40)
for k, v in apro.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*40)
print(f'O jogador {apro["Nome"]} jogou {len(gol)} partidas')
for i, v in enumerate(gol):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {apro["Total"]} gols')