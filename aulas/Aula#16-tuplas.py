lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
# print(lanche[0:2])
# print(lanche[3])
# print(lanche[1:])
# print(lanche[-4])   # Hamburguer    # Conta ao contrário
# print(lanche[-3:])  # Mostra até o final
# print(len(lanche))
# for comida in lanche:
#     print(comida)

# AS TUPLAS SÃO IMUTÁVEIS!

tuplas = ()         # PARENTESES PARA TUPLA
listas = []         # COLCHETES PARA LISTAS
dicionario = {}     # CHAVES PARA DICIONARIOS

# PARENTESES não são obrigatórios em tuplas (mas é bom colocar pra não confundir...)

print(lanche)  # Pra não ficar com a vírgula e parentes...
for comida in lanche:
    print(comida, end=' ')          # "for é uma iteração"

print('\n---------------------------------------')

# for cont in range(0, len(lanche)):
#     print(cont, end=' ')

for pos, comida in enumerate(lanche):       # Experimentar com esse enumerate
    print(f'{comida} na posição {pos}')

print(' ')                              # Essas duas formas... interessante
print(' ')                              # dependendo do que vc quer, serve uma ou outra

for cont in range(0, len(lanche)):
    print(lanche[cont], f'na posição {cont}')

print(' ')
print(' ')

print(sorted(lanche))   # Organizar a tupla (SEM ALTERA-LA)
