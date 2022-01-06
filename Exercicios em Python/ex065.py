n = soma = maior = count = menor = 0
flag = 'S'
while flag == 'S':
    n = int(input('Digite um numero: '))
    count += 1
    soma += n
    flag = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('A média dos numeros digitados é {}, o maior é {} e o menor é {}'.format((soma/count), maior, menor ))
