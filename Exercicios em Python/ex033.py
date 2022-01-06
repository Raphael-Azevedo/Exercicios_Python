n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
maior = n1
if n2 > n1:
    maior = n2
if n3 > maior:
    maior = n3
print('O maior numero é:', maior)
menor = n1
if n2 < n1:
    menor = n2
if n3 < menor:
    menor = n3
print('O menor numero é:', menor)
