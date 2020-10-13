matriz = [[], [], []]
for posy in range(0, 3):
    for posx in range(0, 3):
        valor = (int(input(f'Digite um valor para [{posy}, {posx}]:')))
        if posy == 0:
            matriz[0].append(valor)
        elif posy == 1:
            matriz[1].append(valor)
        elif posy == 2:
            matriz[2].append(valor)
print('-' * 32)
for numero in matriz[0]:
    print(f'[{numero:^5}]', end='')
print('')
for numero in matriz[1]:
    print(f'[{numero:^5}]', end='')
print('')
for numero in matriz[2]:
    print(f'[{numero:^5}]', end='')
print('')
