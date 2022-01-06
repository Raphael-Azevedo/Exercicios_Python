while True:
    print('-'*50)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*25)
    if n < 0:
        break
    for c in range(1, 50):
        print(f'{n} x {c} = {n*c}')
print('Programa tabuada encerrando')
