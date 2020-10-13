galera = list()
dados = []
maiores = []
menores = []
cont = 0
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        mai = men = dados[1]
    if dados[1] > mai:
        mai = dados[1]
    if dados[1] < men:
        men = dados[1]
    galera.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] '))[0]
    if continuar in 'nN':
        break
for dados in galera:
    if dados[1] == mai:
        maiores.append(dados[0])
    elif dados[1] == men:
        menores.append(dados[0])
print('-' * 32)
print(f'foram cadastradas {len(galera)} pessoa(s)')
print(f'O maior peso foi de {max(galera)[1]}kg, de ', end='')   # fiz de duas maneiras
for p in galera:
    if p[1] == max(galera)[1]:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {men}kg, de {menores}')
