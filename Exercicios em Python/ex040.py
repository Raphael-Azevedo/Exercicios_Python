n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2

if m < 5:
    print('A sua média foi {:.2f} você foi REPROVADO'.format(m))
elif m < 7:
    print('A sua média foi {:.2f} você está de RECUPERAÇÃO'.format(m))
elif m >= 7:
    print('A sua média foi {:.2f} PARABÉNSS você foi APROVADO'.format(m))
