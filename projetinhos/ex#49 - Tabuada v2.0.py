n = int(input('Digite um número para ter a sua tabuada: '))
for tab in range(1, 11):
    print('{} x {:2} = {}'.format(n, tab, n * tab))
