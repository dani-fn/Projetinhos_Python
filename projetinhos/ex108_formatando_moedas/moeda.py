def metade(v):
    return v / 2


def dobro(v):
    return v * 2


def aumentar(v, percent=0):
    return v + (v * percent/100)


def diminuir(v, percent=0):
    return v * (1 - percent * 0.01)


def moeda(v, especie='R$'):
    decimais = str(v % 1)[2:4]
    if len(decimais) == 1:
        decimais += '0'
    formatado = f'{especie}{int(v)},{decimais}'
    return formatado
    # Poderia ter feito desta forma:
    # return f'{especie}{v:.2f}'.replace('.', ',')
