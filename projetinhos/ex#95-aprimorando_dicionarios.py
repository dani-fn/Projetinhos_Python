jogadores = list()
jogador = dict()
desempenho = list()
resp = 'S'

while resp not in 'N':
    print('-=' * 20)
    jogador['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    soma = 0
    for partida in range(0, quant):
        gol = int(input(f'{jogador["nome"]} fez quantos gols na partida {partida+1}? '))
        soma += gol
        desempenho.append(gol)
    jogador['gols'] = desempenho[:]
    jogador['total'] = soma
    jogadores.append(jogador.copy())
    desempenho.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] '))[0].upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=-' * 16)
print('cod', end=' ')
for k in jogadores[0].keys():
    print(f'{k:<20}', end=' ')

print('\n', '-' * 48)
for i, v in enumerate(jogadores):
    print(f'{i:3}', end=' ')
    for dado in v.values():
        print(f'{str(dado):<20}', end=' ')  # Foi usado o str() pra não dar erro na formatação
    print()

while True:
    print('-=' * 32)
    qual = int(input('Mostrar dados de qual jogador? (999 p/ parar) '))
    if qual == 999:
        break
    if qual > len(jogadores)-1 or qual < 0:
        print(f'ERRO! Não existe jogador com código {qual}! Tente novamente')
    else:
        print(f'Levantamento do jogador {jogadores[qual]["nome"]}')
        for i, gol in enumerate(jogadores[qual]['gols']):
            print(f'No jogo {i+1} fez {gol} gols')
print()
print('Volte Sempre!')
