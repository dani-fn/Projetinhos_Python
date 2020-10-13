lista = []
pares = []
impares = []
stop = False
while stop is False:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] '))[0]
    if continuar in 'Nn':
        stop = True
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print('-' * 32)
print(f'A lista COMPLETA é {lista}')
print(f'A lista de PARES é {pares}')
print(f'A lista de IMPARES é {impares}')
