from math import hypot
n1 = float(input('Cateto oposto: '))
n2 = float(input('Cateto Adjacente: '))
h = hypot(n1, n2)
print('O comprimento da hipotenusa é de {:.2f}'.format(h))