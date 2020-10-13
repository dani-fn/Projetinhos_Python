lista = [1, 5, 2, 1, 3, 4, 6]
for index, teste in enumerate(lista):
    print(index, teste)

# RUN:
#   (0, 1)
#   (1, 5)
#   (2, 2)
#   (3, 1)
#   (4, 3)
#   (5, 4)
#   (6, 6)
a = '4, 5, 6, 7, 8'
a = a.replace('4', '1')
print(a)
lista = []
for pos in range(0, 5):
    digitado = int(input('Digite um valor: '))
    if pos == 0 or digitado >= lista[-1]:
        lista.append(digitado)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if digitado < lista[pos]:
                lista.insert(pos, digitado)
                print(f'Adicionado na posição [{pos}]...')
                break
            pos += 1
print('-' * 32)
print(f'Os valores digitados em ordem foram: {lista}')
