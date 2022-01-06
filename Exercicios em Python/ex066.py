s = cont = 0
while True:
    n = int(input('Digite um numero(PARA SAIR DIGITE 999): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foi digitado {cont} numeros e a soma entre eles vale {s}')
