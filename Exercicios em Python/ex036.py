from time import sleep
print('-=' * 20)
print("\033[31mSeja Bem Vindo ao Banco Ralph!\033[m")
print('-=' * 20)

valor = float(input('Para iniciar a simulação de crédito por favor digite o valor do imóvel: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Em quanto tempo quer pagar o valor financiado: '))

print('\033[33mPROCESSANDO...\033[m')
sleep(3)
n = valor/(anos * 12)

if n >= (salario * 0.30):
    print('Credito rejeitado, a parcela de RS${:.2f} é superior a 30% do seu salário'.format(n))
else:
    print('PARABÉNS!!! crédito aprovado com {} parcelas de RS${:.2f}'.format((anos*12), n))
