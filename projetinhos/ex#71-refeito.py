print('-' * 28)
print('{:^28}'.format('BANCO DANIMONEY'))
print('-' * 28)
valor = int(input('Quanto deseja sacar? R$'))
total = valor
for ced in [50, 20, 10, 1]:
    quantidade = total // ced
    total = total % ced
    if quantidade > 0:
        print(f'Total de {quantidade} cédulas de R${ced}')

# usando a matematica, sem while
