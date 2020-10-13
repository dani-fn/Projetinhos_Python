valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
# for cont in range(0, 4):                             Tambem posso usar o "input"
#     valores.append(int(input('Digite um valor: ')))

for valor in valores:
    print(f'{valor}...', end='')
print('')
for key, valor in enumerate(valores):  # O enumerate pega tanto a chave quanto o valor
    print(f'Na posição {key}, encontrei {valor}')       # IMPORTANTE
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a                   # a partir do momento que eu igualo duas listas,
b[2] = 8                # o Python cria uma ligação/relação entre elas
print(f'Lista A: {a}')
print(f'Lista B: {b}')  # a lista B NÃO é uma cópia da A


b = a[:]                # Isso sim é tirar cópia
b[2] = 6
print(f'Lista B: {b}')
