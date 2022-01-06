num = []
c = 0
while True:
    n1 = int(input('Digite um numero: '))
    if n1 in num:
        print('Valor duplicado! Não vou adicionar...')
    else:
        num.append(n1)
        print('Valor adicionado com sucesso...')
    c = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while c not in 'SN':
        c = str(input('Digite um valor válido: [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print(f'Os valores que você digitou são {num}')
num.sort()
print(f'Valores ordenados : {num}')
