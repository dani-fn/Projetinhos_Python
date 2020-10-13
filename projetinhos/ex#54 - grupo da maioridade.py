from datetime import date
maior = 0
menor = 0
for loop in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(loop)))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
if menor == 1:
    sppessoa1 = 'pessoa é MENOR'
else:# menor != 1:
    sppessoa1 = 'pessoas são MENORES'
if maior == 1:
    sppessoa2 = 'pessoa é MAIOR'
else:
    sppessoa2 = 'pessoas são MAIORES'
print('{} {} de idade.'.format(menor, sppessoa1))
print('{} {} de idade.'.format(maior, sppessoa2))
