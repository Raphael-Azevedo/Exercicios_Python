n = []
i = 0
for c in range(0, 5):
    n1 = int(input('Digite um valor: '))
    if c == 0 or n1 > n[-1]:
        n.append(n1)
        print(f'Adicionado na posição {c} da lista...')
    else:
        pos = 0
        while pos < len(n):
            if n1 <= n[pos]:
                n.insert(pos, n1)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {n}')
