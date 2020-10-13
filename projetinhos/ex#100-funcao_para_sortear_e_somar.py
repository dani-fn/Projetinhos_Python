from random import randint


def sorteia(q):
    print(f'Sorteando {q} valores da lista:')
    for c in range(0, q):
        num = randint(1, 9)
        print(num, end=' ')
        numeros.append(num)
    print('PRONTO!')


def somapar():
    soma = 0
    print(f'Somando os valores pares de {numeros}, temos', end=' ')
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(soma)


numeros = []
sorteia(5)
somapar()
