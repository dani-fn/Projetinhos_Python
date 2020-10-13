from time import sleep as s
from random import randint
jogo = {}
ranking = {}
print('Valores Sorteados:')
for jogador in range(1, 5):
    s(0.5)
    random = randint(1, 6)
    print(f'    O jogador {jogador} tirou {random}')
    jogo['jogador', jogador] = random
print('Ranking dos jogadores:')        # COMO FUNCIONA LAMBDA E ITEMGETTER?
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)  # key=lambda x: x[1]
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}')

#   O ex-dicionário "ranking" foi transformado em uma lista,
#   por isso, eu usei o "enumerate" que não funciona em dict

#   https://www.w3schools.com/python/python_lambda.asp
#   https://docs.python.org/3/library/operator.html
#   Comparar ex#91 e ex#91a

#   todo MUITO IMPORTANTE ENTENDER TODOS OS COMANDOS DA LINHA 12
