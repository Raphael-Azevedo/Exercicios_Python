dados = []
for c in range(3):
    linha = []
    for y in range(3):
        linha.append(int(input(f'Digite um valor para [{c}, {y}]: ')))
    dados.append(linha)
print('-='*50)
print(f'[ {dados[0][0]} ] [ {dados[0][1]} ] [ {dados[0][2]} ]\n'
      f'[ {dados[1][0]} ] [ {dados[1][1]} ] [ {dados[1][2]} ]\n'
      f'[ {dados[2][0]} ] [ {dados[2][1]} ] [ {dados[2][2]} ]')
