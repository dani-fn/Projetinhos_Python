n = int(input('Quantos termos da sequência de fibonacci deseja ver? '))
cont = 3
t1 = 0
t2 = 1
if n == 0:
    exit()
elif n == 1:
    print('0')
elif n == 2:
    print('{} ► {}'.format(t1, t2), end='')
else:
    print('{} ► {} ► '.format(t1, t2), end='')
    while cont <= n:
        t3 = t1 + t2
        if cont < n:
            print(t3, ' ► ', end='')
        elif cont == n:
            print(t3)
        t1 = t2
        t2 = t3
        cont += 1
