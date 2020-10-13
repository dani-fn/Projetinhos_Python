def metade(v, formatado=True, especie='R$'):
    if formatado:
        return f'{especie}{v / 2:.2f}'.replace('.', ',')
    else:
        return v / 2


def dobro(v, formatado=True):
    if formatado:
        return moeda(v * 2)  # melhor fazer assim
    else:
        return v * 2


def aumentar(v, percent=0, formatado=True, especie='R$'):
    if formatado:
        return f'{especie}{v + (v * percent/100):.2f}'.replace('.', ',')
    else:
        return v + (v * percent/100)


def diminuir(v, percent=0, formatado=True, especie='R$'):
    if formatado:
        return f'{especie}{v * (1 - percent * 0.01):.2f}'.replace('.', ',')
    else:
        return v * (1 - percent * 0.01)


def moeda(v, especie='R$'):
    return f'{especie}{v:.2f}'.replace('.', ',')
