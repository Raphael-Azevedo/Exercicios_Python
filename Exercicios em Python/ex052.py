count = 0
n = int(input('Digite um numero: '))
for c in range(1, n+ 1):
    if n % c == 0:
        count += 1
if count == 2:
    print('O numero {} é um numero primo'.format(n))

else:
    print('Não é um numero primo')
