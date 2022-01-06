def area(a, b):
    m2 = a * b
    print(f'A área de um terreno {a:.2f} x {b:.2f} é de {m2:.2f}m²')


print("Controle de Terrenos")
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
