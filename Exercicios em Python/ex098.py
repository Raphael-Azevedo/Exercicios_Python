from time import sleep


def cont(x, y, p):
    print(f'Contagem de {x} até {y} de {abs(p)} em {abs(p)}')
    if p == 0:
        p = 1
    if y > x:
        y += 1
    elif y < x and p > 0:
        y -= 1
        p *= -1
    elif y < x and p < 0:
        y -= 1
    for c in range(x, y, p):
        print(c, end=' ')
        sleep(0.2)
    print('FIM!')


print('-=' * 20)
x = 1
y = 10
p = 1
cont(x, y, p)
print('-=' * 20)
x = 10
y = 0
p = 2
cont(x, y, p)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
x = int(input('Inicio: '))
y = int(input('Fim: '))
p = int(input('Passo: '))
cont(x, y, p)
