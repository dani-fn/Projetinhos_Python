def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome1 = str(input('Nome do jogador: '))
gols1 = str(input(f'Quantos gols o jogador fez?'))

if gols1.isnumeric():
    gols1 = int(gols1)      # interessante fazer assim
    if nome1.strip() == '':
        ficha(gols=gols1)
    else:
        ficha(nome1, gols1)
else:
    if nome1.isalpha():
        ficha(nome1)
    else:
        ficha()
