lista = [[], []]
for key in range(1, 8):
    num = int(input(f'Digite o {key}o valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 != 0:
        lista[1].append(num)
print('-' * 32)                          # ou: num[0].sort()
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')
