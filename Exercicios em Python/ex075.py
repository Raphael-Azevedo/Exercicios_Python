num = (int(input('Digite um valor: ')), int(input('Digite mais um valor: ')),
       int(input('Digite outro valor: ')), int(input('Digite o ultimo valor: ')))

print('-='*50)
print(f'Você digitou os valores {num}')
print('-='*50)
print(f'O valor 9 apareceu  {num.count(9)} vezes')
print('-='*50)
if 3 in num:
    print(f'O primeiro valor 3 apareceu na posição {num.index(3)+1}')
    print('-=' * 50)
else:
    print('Não foi encontrado o valor 3 na tupla')
    print('-=' * 50)
cont = 0
print('Os numeros pares são:', end=' ')
for c in range(0,4):
    if num[c]% 2 == 0:
        print(num[c],end=' - ')
