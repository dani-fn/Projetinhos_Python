from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),   # <---- Outra forma de fazer
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = dict()
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(0.3)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # key=lambda x: x[1]
for pos, v in enumerate(ranking):
    print(f'{pos+1}º lugar: {v[0]} com {v[1]}')
