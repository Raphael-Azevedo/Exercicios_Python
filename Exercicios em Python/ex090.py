pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
pessoa['Média'] = float(input(f'Média de {pessoa["Nome"]}: '))
if pessoa['Média'] >= 7:
    pessoa['Situação'] = 'Aprovado'
elif 5 <= pessoa['Média'] < 7:
    pessoa['Situação'] = 'Recuperação'
else:
    pessoa['Situação'] = 'Reprovado'
for k, v in pessoa.items():
    print(f'{k} é igual a {v}')

