contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

n = int(input('Digite um numero entre 0 e 20: '))
while n > 20 or n < 0:
    n = int(input('Valor incorreto, Digite novamente um numero entre 0 e 20: '))
print(f'O numero digitado foi {n}, o valor por extenso é {contagem[n]}')
