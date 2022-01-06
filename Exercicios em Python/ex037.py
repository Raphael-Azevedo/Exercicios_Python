n = int(input('Digite um numero: '))
n2 = int(input('''Escolha qual a base de conversão
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL\n'''))

if n2 == 1:
    print('O valor do numero {} em binário é {}'.format(n, (format(n, "b"))))
elif n2 == 2:
    print('O valor do numero {} em octal é {}'.format(n, (format(n, "o"))))
elif n2 == 3:
    print('O valor do numero {} em hexgonal é {}'.format(n, (format(n, "h"))))
else:
    print('Opção invalida')
