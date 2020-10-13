n = int(input('Digite um número: '))
cont = 0
for loop in range(1, n+1):
    if n % loop == 0:
        cont += 1
        print('\033[32m{}\033[m'.format(loop), end=' ')
    else:
        print('\033[31m', loop, end=' ')
print('\nO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:
    print('E por isso, ele \033[32;1mÉ PRIMO')
else:
    print('E por isso, ele \033[31;1mNÃO É PRIMO')
