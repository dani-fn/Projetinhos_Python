from random import randint
from time import sleep
print('\033[7;30m''-=-'*19, '\033[m')
print('\033[7;30mVou pensar em um número entre 0 a 5. Tente adivinhar...   \033[m')
print('\033[7;30m''-=-'*19, '\033[m')
print('PROCESSANDO...')
sleep(1)
num = randint(0, 5)
guess = int(input('\033[1;33mEm que número eu pensei? \033[m'))
if guess == num:
    print('\033[32mDroga! Você acertou! Era mesmo o número \033[1;33m{}\033[32m!\033[m'.format(num))
else:
    print('\033[31mHoje não! Eu pensei no número \033[1;31m{}\033[31m, e não no \033[33m{}\033[m!'.format(num, guess))
