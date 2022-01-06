from datetime import date
dados = dict()

dados['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
dados['Idade'] = date.today().year - ano
dados['Ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: RS$'))
    dados['Aposentadoria'] = dados['Contratação'] + 35 - ano
print('-='*50)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
