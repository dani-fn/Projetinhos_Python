times = ('Athletico-PR', 'Atlético-MG', 'Grêmio', 'Atlético-GO', 'Sport Recife',
         'Bahia', 'Internacional', 'Bragantino-SP', 'Santos', 'Botafogo',
         'Palmeiras', 'Ceará-SC', 'Fluminence', 'São Paulo', 'Vasco da Gama',
         'Corinthians', 'Goiás', 'Coritiba', 'Fortaleza', 'Flamengo')
print('-' * 32)

print('Lista de times do Brasileirão:')
print(times)

print('-' * 32)

print('Os 5 primeiros são:')
print(times[:5])

print('-' * 32)

print('Os 4 últimos são:')
print(times[-4:])

print('-' * 32)

print('Times em ordem alfabética:')
print(sorted(times))

print('-' * 32)

print(f'Palmeiras está em {1 + times.index("Palmeiras")}º')

# print(f'Palmeiras está  em {enumerate(times[10])}º')      PQ DEU ESSE BUG BIZARRO?
