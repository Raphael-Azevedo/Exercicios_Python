n = float(input('Digite o preço do produto: '))
print('As condições de pagamento são:\n1 - A vista 10% de desconto\n2 - A vista no cartão 5% de desconto\n3 - 2x '
      'no cartão preço normal\n4 - 3x no cartão 20% de juros')
n2 = int(input('Digite a condição de pagamento: '))
if n2 == 1:
      print('O preço do seu produto é RS${:.2f}, opção selecionada "A VISTA" total a pagar RS${:.2f}'.format(n, (n*0.90)))
elif n2 == 2:
      print('O preço do seu produto é RS${:.2f}, opção selecionada "A VISTA NO CARTÃO" total a pagar RS${:.2f}'.format(n, (n * 0.95)))
elif n2 == 3:
      print('O preço do seu produto é RS${:.2f}, opção selecionada "2X NO CARTÃO" total a pagar RS${:.2f}'.format(n, (n)))
elif n2 == 4:
      print('O preço do seu produto é RS${:.2f}, opção selecionada "3X OU MAIS NO CARTÃO" total a pagar RS${:.2f}'.format(n, (n * 1.20)))
