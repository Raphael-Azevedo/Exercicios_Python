dados = [[], []]
for c in range(0, 7):
    x = int(input(f'Digite o {c+1}º valor: '))
    if x % 2 == 0:
        dados[0].append(x)
    else:
        dados[1].append(x)
print('-='*50)
print(f'Os valores pares digitados foram: {sorted(dados[0])}')
print(f'Os valores impares digitados foram: {sorted(dados[1])}')