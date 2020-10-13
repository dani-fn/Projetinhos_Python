from time import sleep


def contador(a, b, c):
    print('-==-' * 10)
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if b < a:
        b -= 1
        if c > 0:
            c *= -1
    else:
        b += 1
    for cont in range(a, b, c):
        print(cont, end=' ')
        sleep(0.2)
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print()
print(f'Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
