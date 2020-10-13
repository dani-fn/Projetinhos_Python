print('-' * 24)
print('{:^24}'.format('LOJAS DANNYBOY'))
print('-' * 24)
fim = False
tot = tot1000 = menor = quant = 0
nomebarato = '.'
while fim is False:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    tot += preco
    quant += 1
    if quant == 1 or preco < menor:
        menor = preco
        nomebarato = nome
    if preco >= 1000:
        tot1000 += 1
    mais = ' '
    while mais not in 'sSnN':
        mais = str(input('Algo mais[S/N]? ')).upper()
    if mais in 'nN':
        fim = True
print(f'Total de \033[32;1m{tot:.2f}\033[m reais')
print(f'\033[34;1m{tot1000}\033[m Produto(s) custa(m) ao menos mil reais')
print(f'O produto mais barato é: \033[35;1m{nomebarato}\033[m, custando \033[32;1mR${menor:.2f}\033[m')
