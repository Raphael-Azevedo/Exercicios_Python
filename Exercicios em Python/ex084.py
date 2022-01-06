dado = list()
galera = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    s = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while s not in 'SN':
        s = str(input('Valor incorreto, Deseja continuar? [S/N] ')).strip().upper()[0]
    galera.append(dado[:])
    dado.clear()
    if s == 'N':
        break
print('-='*50)
print(f' Foram cadastradas {len(galera)} pessoas')
for i, v in enumerate(galera):
    if i == 0:
        menor = maior = v[1]
    if v[1] > maior:
        maior = v[1]
    if v[1] < menor:
        menor = v[1]

print(f'O maior peso foi de {maior}KG. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(p[0], end='')
print()
print(f'O menor peso foi de {menor}KG. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(p[0], end='')
