aproveitamento = list()
apro = dict()
gol = list()
cont = 0
while True:
    apro['Nome'] = str(input('Nome do jogador: '))
    partida = int(input(f'Quantas partidas {apro["Nome"]} jogou: '))
    for c in range(0, partida):
        gol.append(int(input(f'Quantos gols na partida {c}? ')))
        cont += gol[c]
    apro['Gols'] = gol.copy()
    apro['Total'] = cont
    cont = 0
    aproveitamento.append(apro.copy())
    apro.clear()
    gol.clear()
    s = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if s == 'N':
        break
    print('-'*50)
print('-='*25)
print(f'{"cod":<4}{"nome":<10}{"gols":<15}{"total":>20}')
print('-'*50)
for c in range(0, len(aproveitamento)):
    print(f'{c:<4}{aproveitamento[c]["Nome"]:<10}{str(aproveitamento[c]["Gols"]):<15}{aproveitamento[c]["Total"]:>20}')
print('-'*50)
while True:
    levantamento = int(input('Mostrar dados de qual jogador? '))
    if levantamento == 999:
        break
    if levantamento > len(aproveitamento) - 1:
        print(f'ERRO! não existe jogador com código {levantamento}! Tente novamente')
        print('-' * 50)
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {aproveitamento[levantamento]["Nome"]}:')

        for i, v in enumerate(aproveitamento[levantamento]["Gols"]):
            print(f'=> Na partida {i}, fez {v} gols.')
        print('-' * 50)
print('<< VOLTE SEMPRE >>')
