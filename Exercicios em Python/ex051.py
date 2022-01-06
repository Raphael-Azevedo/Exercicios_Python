n1 = int(input('Digite o primeiro termo da PA: '))
n2 = int(input('Digite a razão da PA: '))
for c in range(1, 11):
    o = n1 + (c - 1)*n2
    print(o, end=' - ')
print('ACABOU')