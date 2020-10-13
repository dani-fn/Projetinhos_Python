def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (optional) mostrar ou não a conta
    :return: O valor do fatorial do número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(c, 'x ', end='')
            else:
                print('1 = ', end='')
        f *= c
    return f


print()
print(fatorial(4, True))
help(fatorial)
