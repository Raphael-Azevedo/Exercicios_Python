n1 = int(input('Digite o valor do fatorial: '))
c = n1
f = 1
print('Calculando {}!'.format(n1))
for c in range(n1, 0, -1):
    print('{} '.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end='  ')
    f *= c
print('{}'.format(f))

'''n1 = int(input('Digite o valor do fatorial: '))
c = n1
f = 1
print('Calculando {}!'.format(n1))
while c > 0:
    print('{} '.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end='  ')
    f *= c
    c -= 1
print('{}'.format(f))'''