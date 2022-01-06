from datetime import date
ano = int(input('Qual o seu ano de nascimento: '))
idade = date.today().year - ano

if idade > 18:
    print('Já passou {} anos do tempo do seu alistamento militar!'.format(idade - 18))
elif idade == 18:
    print('É a hora de se alistar!')
elif idade < 18:
    print('Você ainda vai se alistar ao serviço militar! falta {} anos'.format(18 - idade))
