print('*' * 42)
print('{:^42}'.format('10 termos de uma P.A definida por você!'))
print('*' * 42)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n10 = n1 + (10 - 1) * r
for pa in range(n1, n10 + r, r):
    print(pa, ' ► ', end='')
print('FIM')
