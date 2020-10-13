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
                print(f'Adicionado na posição [{pos}]')
                break
            pos += 1
print('-' * 32)
print(f'Os valores digitados em ordem foram {lista}')

# usar len() ou [-1]
# ir ciclando pelas posições e comparando...
