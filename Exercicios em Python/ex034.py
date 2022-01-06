n = float(input('Digite o valor do salario: '))
if n >= 1250:
    print('Seu salario atual é RS${} o seu novo salario será de RS${:.2f}'.format(n, n * 1.10))
else:
    print('Seu salario atual é RS${}, o seu novo salario será de RS${:.2f}'.format(n, n * 1.15))
