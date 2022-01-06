num = []
par = []
impar = []
c = 0
while True:
    num.append(int(input('Digite um numero: ')))
    s = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    """if num[c] % 2 == 0:
        par.append(num[c])
    else:
        impar.append(num[c])
    c += 1"""
    if 'N' in s:
        break
    while 'S' not in s:
        s = str(input('Valor incorreto, Digite novamente: [S/N] ')).upper().strip()[0]
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-='*30)
print(f'Os numeros digitados foram: {num}\n'
      f'Os numeros pares foram: {par}\n'
      f'Os numeros impares foram: {impar}')
