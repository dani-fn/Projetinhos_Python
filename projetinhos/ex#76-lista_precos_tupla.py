from emoji import emojize
print('\033[30m-' * 32)
print('{:^32}'.format(emojize('Livraria \033[31;1mGigi Amor :red_heart:')))  # "use_aliases=True" Pra que serve??
print('\033[30m-\033[m' * 32)
itens = ('Som do amor', 31,
         'Antes de você', 40,
         'Depois de você', 35,
         'Senhor dos anéis', 50,
         'Labirinto dos espíritos', 42.50,
         'Jogo do anjo', 34.90,
         'Corte espinhos e rosas', 30.50,
         'Crônicas de Nárnia', 65.99,
         'Rainbow', 24.60)
print('')
cont = 0
for tabela in itens[::2]:                   # OU:   for pos in range(0, len(itens)):
    print(f'{tabela:.<32} R$', end='')      # ...       if pos % 2 == 0:
    cont += 1
    print(f'{itens[cont]:>6.2f}')
    cont += 1
print('')
print('\033[30m-\033[m' * 32)
