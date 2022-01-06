n = str(input('Digite seu nome: ')).strip()
n2 = n.split()
print('Seu primeiro nome é {}'.format(n2[0]))
print('Seu ultimo nome é {}'.format(n2[len(n2)-1]))
