dados = []
soma = soma2 = maior = 0
for c in range(3):
    linha = []
    for y in range(3):
        x = int(input(f'Digite um valor para [{c}, {y}]: '))
        linha.append(x)
        if x % 2 == 0:
            soma += x
        if y == 2:
            soma2 += x
        if c == 1 and x > maior:
            maior = x
    dados.append(linha[:])
print('-='*30)
print(f'[ {dados[0][0]} ] [ {dados[0][1]} ] [ {dados[0][2]} ]\n'
      f'[ {dados[1][0]} ] [ {dados[1][1]} ] [ {dados[1][2]} ]\n'
      f'[ {dados[2][0]} ] [ {dados[2][1]} ] [ {dados[2][2]} ]')
print('-='*30)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma2}')
print(f'O maior valor da segunda linha é {maior}')
