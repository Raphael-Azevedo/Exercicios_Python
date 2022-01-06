n = count = soma = 0
n = int(input('Digite um numero: '))
print('Para para digite 999')
while n != 999:
    count += 1
    soma += n
    n = int(input('Digite um numero: '))
    print('Para para digite 999')
print('A quantidade de numeros digitado foi {} e a soma entre eles é {}'.format(count, soma))
