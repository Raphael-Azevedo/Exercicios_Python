palavras = ('Azul', 'Amarelo', 'Voar', 'Vencer')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos', end=' ')
    for p in c:
        if p.lower() in 'aeiou':
            print(p, end='')