c = c2 = c3 = c4 = 0
n = int(input('Digite o valor a ser sacado: '))
soma = n
while True:
    if soma >= 50:
        c += 1
        soma -= 50
    elif soma >= 20:
        c2 += 1
        soma -= 20
    elif soma >= 10:
        c3 += 1
        soma -= 10
    elif soma >= 1:
        c4 += 1
        soma -= 1
    if soma == 0:
        break
print(f'''O valor a ser sacado é RS$ {n:.2f}
{c} notas de RS$50,00
{c2} notas de RS$20,00
{c3} notas de RS$10,00
{c4} notas de RS$1,00''')