valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        menor = maior = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if menor > valores[c]:
            menor = valores[c]
print(f'Os valores digitados foram: {valores}')
print(f'O maior numero digitado é {maior} na posição', end=' ')
for i, n in enumerate(valores):
    if n == maior:
        print(f'{i+1}...', end='')
print()
print(f'O menor numero digitado é {menor} na posição', end= ' ')
for i, n in enumerate(valores):
    if n == menor:
        print(f'{i+1}...', end='')