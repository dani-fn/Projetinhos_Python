matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sompar = som3c = mai2l = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-' * 32)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            sompar += matriz[linha][coluna]
        if coluna == 2:
            som3c += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0 or matriz[linha][coluna] > mai2l:
                mai2l = matriz[linha][coluna]
    print()
print('-' * 32)
print(f'A soma dos valores pares é {sompar}')
print(f'A soma dos valores da terceira coluna é {som3c}')
print(f'O maior valor da segunda linha é {mai2l}')
