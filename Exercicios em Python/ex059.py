n = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
escolha = 0
while escolha != 5:
    print('''ESCOLHA A OPERAÇÃO'
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5]sair do programa''')
    escolha = int(input('Qual é a sua opção? '))
    if escolha == 1:
        print('A soma dos numeros é {}'.format(n + n2))
    elif escolha == 2:
        print('O produto dos dois numeros é {}'.format(n*n2))
    elif escolha == 3:
        if n > n2:
            print('O valor {} é maior que o numero {}!'.format(n, n2))
        elif n < n2:
            print('O valor {} é maior que o valor {}!'.format(n2, n))
    elif escolha == 4:
        n = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
    else:
        escolha = int(input('VALOR INVALIDO\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5]sair do programa\n'))


