from random import randint
c = 0
print('-=' * 10)
print('JOGO DO PAR OU IMPAR')
print('-=' * 10)
while True:
    n = int(input('Digite um valor: '))
    s = str(input('Par ou impar?[P/I] ')).upper().strip()[0]
    while s not in 'PI':
        s = str(input('Par ou impar?[P/I] ')).upper().strip()[0]
    r = randint(0, 100)
    print('-' * 55)
    if (n + r) % 2 == 0:
        par = 'PAR'
        p = 'P'
    else:
        par = 'IMPAR'
        p = 'I'
    print(f'Você jogou {n} e o computador {r}. Total de {n + r} DEU {par}')
    print('-' * 55)
    if p == s:
        print('Você VENCEU!!\nJogue novamente...')
        c += 1
    if p != s:
        print('Você perdeu!')
        break
print(f'GAME OVER você venceu {c} vezes')
