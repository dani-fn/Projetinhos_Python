casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
meses = anos * 12
prest = casa / meses
if prest > sal * 30 / 100:
    print("""O empréstimo do valor de R${} com prestações mensais de R${:.2f}
a serem pagas durante um período de {} anos é:
\033[31mNEGADO""".format(casa, prest, anos))
else:
    print('O empréstimo do valor de R${} com prestações mensais de R${:.2f}'.format(casa, prest), end=' ')
    print('a serem pagas durante um perídodo de {} anos é:'.format(anos))
    print('\033[32mAPROVADO')
