lista = []
fechar = ' '
while fechar not in 'nN':
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    fechar = str(input('Quer continuar? [S/N]'))[0]
print('-' * 32)
print(f'Você digitou os valores {sorted(lista)}')