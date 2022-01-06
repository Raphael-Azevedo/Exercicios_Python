from datetime import date
count = 0
for c in range(0, 6):
    n = int(input('Digite a data de nascimento: '))
    idade = date.today().year - n
    if idade > 21:
        count += 1
print('Ha {} pessoas maior de idade e {} que ainda não são'.format(count, (6-count)))
