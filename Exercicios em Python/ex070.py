soma = count = p = 0
while True:
    print('-' * 30)
    print('     CAIXA     ')
    print('-' * 30)
    produto = str(input('Produto: '))
    preco = float(input('Preço: RS$ '))
    soma += preco
    if preco >= 1000:
        count += 1
    if p == 0 or preco < p:
        p = preco
        prod = produto
    s = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while s not in 'SN':
        s = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if s == 'N':
        break
print(f'O total gasto na compra é RS${soma:.2f}'
      f'Foram {count} produtos com preço acima de RS$1000,00'
      f'O produto mais barato é {prod} que custa RS${p:.2f}')
