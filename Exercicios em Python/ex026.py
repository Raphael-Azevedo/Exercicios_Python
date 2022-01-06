n = str(input('Digite uma frase: ')).upper().strip()
print('A letra a aparece {}'.format(n.count('A')))
print('A primeira letra A paraceu na posição {}'.format(n.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(n.rfind('A')+1))
