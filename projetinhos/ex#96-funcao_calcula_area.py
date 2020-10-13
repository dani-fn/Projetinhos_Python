def lin20():
    print('-' * 20)


def area():
    width = float(input('Largura: (m) '))
    length = float(input('Comprimento: (m) '))
    metragem = width * length
    print(f'A área do terreno de dimensões {width} x {length} é de {metragem} m²')


print('Controle de terrenos')
print('-' * 20)
area()
