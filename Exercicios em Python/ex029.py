v = float(input('Qual a velocidade do carro? '))
if v >= 80:
    multa = (v-80)*7
    print('Voce passou do limite de velocidade, a sua velocidade foi {} e a multa será de RS${:.2f}'.format(v, multa))
else:
    print('A sua velocidade é de {}'.format(v))
