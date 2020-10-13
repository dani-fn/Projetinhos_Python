print('-' * 28)
print('{:^28}'.format('BANCO DANIMONEY'))
print('-' * 28)
valor = int(input('Quanto deseja sacar? R$'))
total = valor
ced50 = total // 50
total %= 50
ced20 = total // 20
total %= 20
ced10 = total // 10
total %= 10
ced1 = total // 1
total %= 1
if ced50 > 0:
    print(f'Total de {ced50} cédulas de R$50')
if ced20 > 0:
    print(f'Total de {ced20} cédulas de R$20')
if ced10 > 0:
    print(f'Total de {ced10} cédulas de R$10')
if ced1 > 0:
    print(f'Total de {ced1} cédulas de R$1')
