lista = []
pos5 = []
key5 = 0
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = str(input('Quer continuar? [S/N] '))[0]
    if continuar in 'Nn':
        break
print('-' * 32)
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if lista.count(5) > 0:
    for key5, cincos in enumerate(lista):
        if cincos == 5:
            pos5.append(key5)
    print(f'O valor 5 foi encontrado em: {pos5}')
else:
    print('O valor 5 não foi encontrado na lista.')
