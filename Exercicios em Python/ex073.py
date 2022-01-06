times = ('Atlético - MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Internacional', 'Corinthians', 'Fluminense', 'Atlético - GO', 'América - MG', 'Cuiabá', 'Athletico - PR', 'São Paulo', 'Ceará SC', 'Bahia', 'Santos', 'Juventude', 'Sport Recife', 'Grêmio', 'Chapecoense')
print('-='*50)
print(f'Os cincos primeiro colocado são {times[:5]}')
print('-='*50)
print(f'Os ultimos 4 colocados da tabéla são {times[16:]}')
print('-='*50)
print(sorted(times))
print('-='*50)
print('O Chapecoense está na {} posição'.format(times.index('Chapecoense')+1))


