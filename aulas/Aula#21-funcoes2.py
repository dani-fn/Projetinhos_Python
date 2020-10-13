# Importação global e importação local, qual a diferença?
def somar(a=0, b=0, c=0):
    s = a + b + c
    return a and s


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
print(somar(3, 2, 5))


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')


num = int(input('Digite um número: '))
if par(num):    # posso fazer assim pq é um valor booleano
    print('É par!')
else:
    print('Não é par!')
