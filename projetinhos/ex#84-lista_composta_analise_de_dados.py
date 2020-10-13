galera = list()
dados = []
maiores = []
menores = []
cont = 0
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    cont += 1
    if cont == 1:
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
print(f'O maior peso foi de {mai}kg, de {maiores}')
print(f'O menor peso foi de {men}kg, de {menores}')
