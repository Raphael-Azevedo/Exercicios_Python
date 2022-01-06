c = c2 = c3 = 0

while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA     ')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    if idade < 18:
        c += 1
    if sexo == 'M':
        c2 += 1
    if sexo == 'F' and idade < 20:
        c3 += 1
    print('-' * 30)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    while continuar not in 'SN':
        print('-' * 30)
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('-' * 30)
print(f'Foram contadas {c} pessoas com menos de 18 anos, {c2} homens e {c3} mulheres com menos de 20 anos.')
print('='*5,'FIM DO PROGRAMA','='*5)