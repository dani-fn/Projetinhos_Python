tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('{:=^20}'.format('FIM'))
# print(f'{"FIM":=^20}')    VERSÃO NOVA
# AGORA SIMPLIFICADO:

tempo = int(input('Quantos anos tem o seu carro? '))
print('carro novo'if tempo <= 3else'carro velho')
print('{:=^20}'.format('FIM'))
