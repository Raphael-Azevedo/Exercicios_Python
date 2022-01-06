h = 0
i2 = 0
i3 = 0
for c in range(0, 4):
    n = str(input('Digite seu nome: ')).strip()
    i = int(input('Digite sua idade: '))
    s = str(input('Digite seu sexo: ')).strip().upper()
    i2 += i
    if i > h and s == 'MASCULINO':
        h = i
        m = n
    if i < 20 and s == 'FEMININO':
        i3 += 1

print('A media de idade é {}, o homem mais velho é {} e tem {} mulheres com menos de 20 anos'.format((i2/4), m, i3))
