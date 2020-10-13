print('*'*16)
print('Sequência de Fibonacci')
print('*'*16)
n = int(input('Quantos elementos você quer mostrar? '))
t1 = 0
t2 = 1
if n == 0:
    exit()
elif n == 1:
    print(t1)
elif n == 2:
    print(t1, ' ► ', t2)
else:
    print(t1, '►', t2, '► ', end='')
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        print(t3, '► ' if cont < n else '', end='')
        t1 = t2
        t2 = t3
        cont += 1
