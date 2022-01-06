n1 = int(input('Digite o primeiro termo da PA: '))
n2 = int(input('Digite a razão da PA: '))
termo = n1
f = 10
total = 0
c = 1
while f != 0:
    total += f
    while c <= total:
        print(' {} -'.format(termo), end='')
        termo += n2
        c += 1
    print(' PAUSA')
    f = int(input('Quantos numeros mais gostaria de ver: '))
print('FIM')

'''n1 = int(input('Digite o primeiro termo da PA: '))
n2 = int(input('Digite a razão da PA: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end=' ')
        termo += n2
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')'''