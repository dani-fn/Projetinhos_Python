from math import factorial
n = int(input('Digite um número para saber seu fatorial: '))
sequence = 0
while sequence != 2:
    if n == 1 or n == 0:
        sequence = 2
        print('!{} '.format(n), end='')
    else:
        print('!{} = '.format(n), end='')
        for sequence in range(n, 1, -1):
            print(sequence, 'x ', end='')
        print('1 ', end='')
    print('= {}'.format(factorial(n)))
