v = float(input('Digite a distancia em km da sua viagem: '))
if v <= 200 :
    print('O valor da sua viagem será de RS${:.2f}'.format(0.5*v))
else:
    print('O valor da sua viagem será de RS${:.2f}'.format(0.45*v))
