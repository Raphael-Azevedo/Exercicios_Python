f = str(input('Digite uma frase: ')).strip().upper()
palavras = f.split()
f2 = ''.join(palavras)
f3 = f2[::-1]
'''for c in range((len(f2)-1), -1, -1):
    f3 += f2[c]'''
print(f3)
print(f2)
if f3 == f2:
    print('A frase é um palindromo')
else:
    print('A frase não é palindromo')
