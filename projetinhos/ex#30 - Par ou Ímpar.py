n = int(input('Digite um número: '))
if n % 2 == 0:
    print('\033[37m{} é um número PAR'.format(n))
else:
    print('\033[37m{} é um número ÍMPAR'.format(n))
