peso = 0
peso2 = 9999
for c in range(0,5):
    n = float(input('Digite seu peso: '))
    if n > peso:
        peso = n
    if n < peso2:
        peso2 = n

print('O maior peso é {} Kg e o menor peso é {} Kg'.format(peso, peso2))
