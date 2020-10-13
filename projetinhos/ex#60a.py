n = int(input('Digite um número para saber o seu fatorial: '))
c = n
f = 1           # "1" é o fator nulo da multiplicação, assim como "0" é o fator nulo da soma e subtração
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
