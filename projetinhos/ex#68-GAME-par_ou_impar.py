from random import randint
from time import sleep
cont = 0
print('-'*25)
print('Vamos jogar PAR ou ÍMPAR!')
while True:
    print('-' * 25)
    n = int(input('Digite um valor: '))
    guess = str(input('Par ou ímpar? [P/I] ')).strip().upper()  # [0] para pegar o primeiro caractere
    cpu = randint(1, 10)
    if (n+cpu) % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print('-' * 54)
    print(f'Você jogou {n} e o computador jogou {cpu}. Total de {n+cpu} ► {result}')
    print('-' * 54)
    if guess == result[0]:
        print('VOCÊ VENCEU!')
        cont += 1
        print('Vamos jogar novamente', end=''), sleep(1)
        print('.', end=''), sleep(0.5)
        print('.', end=''), sleep(0.5)
        print('.'), sleep(0.5)
    else:
        print('VOCÊ PERDEU!')
        break
print(f'GAME OVER! Você venceu {cont} vez(es).')
