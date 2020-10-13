from random import choice
from time import sleep
from sys import exit
print('''Suas opções:
\033[30m[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA\33[m''')
jogada = int(input('Qual a sua jogada? '))
if jogada == 1:
    jogada = 'PEDRA'
elif jogada == 2:
    jogada = 'PAPEL'
elif jogada == 3:
    jogada = 'TESOURA'
else:
    exit('PÊÊÊÊÊÊÊÊ!!! Digite uma jogada válida!')
print('\033[33mJO...')
sleep(0.8)
print('KEN...')
sleep(0.8)
print('\033[32;1mPO!!!\033[m')
sleep(0.5)
cpu = choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('\033[35;1m*\033[m' * 26)
print('CPU escolheu \033[30;1m{}\033[m'.format(cpu))
print('Jogador escolheu \033[30;1m{}\033[m'.format(jogada))
print('\033[35;1m*\033[m' * 26)
if cpu == jogada:
    print('\033[33;1mEMPATE!!!')
elif cpu == 'PEDRA' and jogada == 'TESOURA'\
        or cpu == 'PAPEL' and jogada == 'PEDRA'\
        or cpu == 'TESOURA' and jogada == 'PAPEL':
    print('\033[31;1mVOCÊ PERDEU!\033[31m O Computador sai vitorioso!')
else:
    print('\033[32;1mVOCÊ GANHOU!\033[32m PARABÉNS!')
