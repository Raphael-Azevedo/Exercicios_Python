s = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Valor invalido, digite seu sexo novamente [F/M]: ')).strip().upper()[0]
print('Cadastro feito com sucesso')