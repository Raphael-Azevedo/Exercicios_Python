from random import choice
jogo = str(input('Escolhe PEDRA, PAPEL OU TESOURA: ')).upper().strip()
computador = choice(['PEDRA', 'PAPEL', 'TESOURA'])

if jogo == computador:
    print('Você escolheu {}, o computador {}, resultado EMPATE!'.format(jogo, computador))
elif (jogo == 'PEDRA' and computador == 'TESOURA') or (jogo == 'PAPEL' and computador == 'PEDRA') or (jogo == 'TESOURA' and computador == 'PAPEL'):
    print('Você escolheu {}, o computador {}, PARABÉNS VOCÊ GANHOU!!'.format(jogo, computador))
elif (jogo == 'TESOURA' and computador == 'PEDRA') or (jogo == 'PEDRA' and computador == 'PAPEL') or (jogo == 'PAPEL' and computador == 'TESOURA'):
    print('Você escolheu {}, o computador {}, VOCê PERDEU!'.format(jogo, computador))
else:
    print('Entrada invalida')
