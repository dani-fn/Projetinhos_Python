print('*' * 15)
print('GERADOR DE P.A')
print('*' * 15)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
c = 1
while c <= 10:
    print(a1, ' ► ' if c < 10 else '', end='')
    c += 1
    a1 += r
