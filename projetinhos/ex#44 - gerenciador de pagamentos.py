print('\033[35;1m{:*^48}\033[m'.format(' Lojas Daniel '))
p = float(input('Preço das compras: R$'))
forma = int(input('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual sua opção? '''))
if forma == 1:
    print('Sua compra de R${:.2f} custará R${:.2f}'.format(p, p - p * 10 / 100))    # Desconto de 10%
elif forma == 2:
    print('Sua compra de R${:.2f} custará R${:.2f}'.format(p, p * 0.95))            # Desconto de 5%
elif forma == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(p / 2))
    print('Sua compra custará R${:.2f}'.format(p))
elif forma == 4:
    vezes = int(input('Quantas Parcelas? '))
    pfinal = p * 1.2
    print('Sua compra será parcelada em {:.2f}x de R${:.2f} COM JUROS.'.format(vezes, pfinal / vezes))  # Juros de 20%
    print('Sua compra de R${:.2f} custará R${:.2f}'.format(p, pfinal))
else:
    print('\033[31;1mSelecione uma opção válida!')
