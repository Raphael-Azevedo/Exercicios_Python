n = int(input('Digite um numero: '))
t1 = 0
t2 = 1
c = 3
print('{} - {}'.format(t1, t2), end=' - ')
while c <= (n):
    t3 = t1 + t2
    c += 1
    print('{}'.format(t3), end=' - ')
    t1 = t2
    t2 = t3
print ('FIM')