n1 = int(input('Digite o primeiro termo da PA: '))
n2 = int(input('Digite a razão da PA: '))
count = 1
while count != 11:
    o = n1 + (count - 1)*n2
    count += 1
    print(o, end=' - ')
print('ACABOU')