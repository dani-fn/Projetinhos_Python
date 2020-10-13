from random import randint
from time import sleep


def maior(* num):
    print('-=' * 16)
    print('Analisando os valores passados...')
    for v in num:
        print(v, end=' ')
        sleep(0.3)
    if len(num) > 0:
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')
    else:
        print(f'Não foi informado nenhum valor')


maior(randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
maior(randint(1, 9), randint(1, 9), randint(1, 9))
maior(randint(1, 9), randint(1, 9))
maior(randint(1, 9))
maior()
