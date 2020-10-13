jogador = dict()
desempenho = list()
jogador['nome'] = str(input('Nome do jogador: '))
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
total = 0
for partida in range(0, quant):
    desempenho.append(int(input(f'Quantos gols na partida {partida}? ')))
    total += desempenho[partida]
jogador['gols'] = desempenho[:]
jogador['total'] = total
print('-' * 32)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-' * 32)
print(f'O jogador {jogador["nome"]} jogou {len(desempenho)} partidas')
for i, v in enumerate(desempenho):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {total} gols.')
