from time import sleep
from random import randint
lista = []
jogos = []
print('-' * 32)
print(f'{"MEGA SENA":^32}')
print('-' * 32)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{"  Sorteando" f" {quant} " "Jogos  ":*^32}')
sleep(0.3)
cont = 0
for indexjogo in range(quant):
    while cont < 6:
        random = randint(1, 59)         # sorted(sample(range(1, 61), 6))   é mais prático
        if random not in lista:
            lista.append(random)
            cont += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    cont = 0
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.4)
print(f'{" < BOA SORTE! > ":-^32}')
