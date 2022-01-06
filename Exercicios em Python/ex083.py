exp = []
x = str(input('Digite uma expressão: ')).strip()
for c in x:
    if c == '(':
        exp.append('(')
    elif c == ')':
        if len(exp) > 0:
            exp.pop()
        else:
            exp.append(')')
            print(len(exp))
            break
if len(exp) == 0:
    print('Expressão válida!')
else:
    print('Expressão invalida!')