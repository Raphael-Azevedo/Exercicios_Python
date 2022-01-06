from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('Você tem {} anos. A sua categoria é MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('Você tem {} anos. A sua categoria é INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('Você tem {} anos. A sua categoria é JUNIOR'.format(idade))
elif 19 < idade <= 20:
    print('Você tem {} anos. A sua categoria é SÊNIOR'.format(idade))
elif idade > 20:
    print('Você tem {} anos. A sua categoria é MASTER'.format(idade))
else:
    print('Idade invalida')