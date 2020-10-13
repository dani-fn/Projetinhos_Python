jogador = dict()
desempenho = list()
jogador['nome'] = str(input('Nome do jogador: '))
quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
soma = 0
for partida in range(0, quant):
    gol = int(input(f'{jogador["nome"]} fez quantos gols na partida {partida}? '))
    soma += gol
    desempenho.append(gol)
jogador['gols'] = desempenho[:]
jogador['total'] = soma
print('-=-' * 12)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-' * 36)
print(f'O jogador {jogador["nome"]} jogou {len(desempenho)} partidas')
for k, v in enumerate(desempenho):
    print(f'    =>  Na partida {k}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols.')
