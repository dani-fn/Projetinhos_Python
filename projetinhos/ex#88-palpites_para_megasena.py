from time import sleep
from random import randint
lista = []
print('-' * 32)
print(f'{"MEGA SENA":^32}')
print('-' * 32)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{"  Sorteando" f" {jogos} " "Jogos  ":*^32}')
sleep(0.3)
cont = 0
for indexjogo in range(jogos):
    print(f'Jogo {indexjogo+1}: ', end='')
    while cont < 6:
        random = randint(1, 61)         # sorted(sample(range(1, 61), 6))
        if random not in lista:
            lista.append(random)
            cont += 1
    print(sorted(lista))
    lista.clear()
    cont = 0
    sleep(0.5)
print(f'{" < BOA SORTE! > ":-^32}')
