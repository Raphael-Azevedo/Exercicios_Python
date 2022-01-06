p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))

imc = p / (a**2)

if imc <= 18.5:
    print('Seu imc é {:.2f} você está abaixo do peso'.format(imc))
elif 18.5 < imc <= 25.0:
    print('Seu imc é {:.2f} você está no peso ideal'.format(imc))
elif 25.0 < imc <= 30.0:
    print('Seu imc é {:.2f} você está no sobrepeso'.format(imc))
elif 30.0 < imc <= 40.0:
    print('Seu imc é {:.2f} você está obeso'.format(imc))
elif imc > 40.0:
    print('Seu imc é {:.2f} você é obeso mórbido'.format(imc))
