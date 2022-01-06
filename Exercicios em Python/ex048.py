s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c)
        s += c
print('A soma dos numeros é {}'.format(s))
