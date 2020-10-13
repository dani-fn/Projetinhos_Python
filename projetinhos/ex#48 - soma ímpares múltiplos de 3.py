soma = 0
contador = 0
for loop1 in range(3, 500, 2):
    if loop1 % 3 == 0:
        soma += loop1
        contador += 1
print('A soma de todos os {} valores solicitados é {}'.format(contador, soma))
