from random import randint


def mensagem(txt):
    """

    :param txt:
    :return:
    """
    print('-' * 16)
    print(txt)
    print('-' * 16)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


mensagem(input('Escreva algo: '))

# a = randint(1, 6)
# b = randint(1, 6)
soma(randint(1, 6), randint(1, 6))
