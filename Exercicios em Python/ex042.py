r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 != r2 != r3 != r1:
        print('Os seguimentos acima PODEM FORMAR um triangulo ESCALENO!')
    elif r1 == r2 == r3:
        print('Os seguimentos acima PODEM FORMAR um triangulo EQUILÁTERO!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Os seguimentos acima PODEM FORMAR um triangulo ISÓSCELES!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triangulo!')
