num = []

while True:
    num.append(int(input('Digite um numero: ')))
    s = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if 'N' in s:
        break
    while 'S' not in s:
        s = str(input('Valor incorreto, Digite novamente: [S/N] ')).upper().strip()[0]
print('-='*50)
print(f'Foram digitados {len(num)} numeros')
num.sort(reverse=True)
print(num)
if 5 in num:
    print('A lista contem o numero 5!')
else:
    print('A lista não tem o numero 5!')