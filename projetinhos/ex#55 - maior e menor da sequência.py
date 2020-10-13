maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('peso da {}ª pessoa em kg: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))
