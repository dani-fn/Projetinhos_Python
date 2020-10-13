from random import randint
escolhas = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0, 2)
print('O computador escolheu {}'.format(escolhas[cpu]))
