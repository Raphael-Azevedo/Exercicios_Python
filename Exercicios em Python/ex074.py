from random import randint
listagem = (randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999))
print(listagem)
print(f'O maior numero é {max(listagem)} e o menor é {min(listagem)}')