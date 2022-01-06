dados = dict()
populacao = list()
cont = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    dados['Idade'] = int(input('Idade: '))
    populacao.append(dados.copy())
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-='*50)
print(f'O grupo tem {len(populacao)} pessoas.')
for c in range(0, len(populacao)):
    cont += populacao[c]['Idade']
print(f'A média de idade é de {cont/len(populacao):.2f} anos')
print('As mulheres cadastradas foram:', end=' ')
for s in range(0, len(populacao)):
    if populacao[s]['Sexo'] == 'F':
        print(f'{populacao[s]["Nome"]}', end=' ')
print('')
print('Lista das pessoas que estão acima da média: ')
for p in range(0, len(populacao)):
    if populacao[p]['Idade'] >= (cont/len(populacao)):
        print(f'{populacao[p]}')
print('<< ENCERRADO >>')