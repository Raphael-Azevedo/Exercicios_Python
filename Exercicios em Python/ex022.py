nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maisculo é {}.'.format(nome.upper()))
print('Seu nome com todas as letras em minuscula é',nome.lower())
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))

n3 = nome.split()
print('Seu nome tem {} palavras'.format(len(n3)))

