from random import randint
from time import sleep
print('\033[7;30m''-=-'*19, '\033[m')
print('\033[7;30mVou pensar em um número entre 0 a 10. Tente adivinhar...  \033[m')
print('\033[7;30m''-=-'*19, '\033[m')
sleep(1)
print('PROCESSANDO', end=''), sleep(0.3)
print('.', end=''), sleep(0.3)
print('.', end=''), sleep(0.3)
print('.'), sleep(0.2)
num = randint(0, 10)
guess = int(input('\033[1;33mEm que número eu pensei? \033[m'))    # Tem como fazer com:      acertou = False
count = 1                                                          # ...                      while not acertou:
while guess != num:                                                # ...                          if guess = num
    if guess < num:                                                # ...                              acertou = True
        dica = 'MAIOR'
    else:
        dica = 'MENOR'
    guess = int(input('\033[31;1mVOCÊ ERROU! \033[35;1m{}\033[m'
                      '\n\033[33mTente novamente: \033[m'.format(dica)))
    count += 1
print('\033[32;1m*****VOCÊ ACERTOU!*****\033[m'
      '\nEra o número \033[33;1m{}\033[m'.format(num))
if count == 1:
    print('Você levou {} tentativa para acertar!'.format(count))
else:
    print('Você levou {} tentativas para acertar!'.format(count))
