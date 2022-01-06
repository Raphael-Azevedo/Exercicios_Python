lista = [
    ['p1', 13],
    ['p2', 3],
    ['p3', 23],
    ['p4', 43],
    ['p5', 8]
]

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)
