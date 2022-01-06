def contador(*num):
    print('-='*30)
    print('Analisando os valores passados ...')
    print(f'{num} foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        print(f'O maior valor informador foi 0.')
    else:
        print(f'O maior valor informador foi {max(num)}.')


contador(2, 9, 4, 5, 7, 1)
contador(4, 7, 0)
contador(1, 2)
contador(6)
contador()
