def titulo(msg, cor='\033[m'):
    print(cor, '~' * (len(msg) + 4))
    print(f'   {msg}  ')
    print(cor, '~' * (len(msg) + 4))


def ajudacor(codigo, cor):
    from time import sleep
    sleep(0.5)
    print(cor, end='')
    help(codigo)


print('')
titulo('Sistema de ajuda PyHELP', '\033[30;1;42m')
while True:
    comando = str(input('\033[m("fim" para sair) Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    titulo(f'Acessando o manual do comando "{comando}"', '\033[44;30;1m')
    ajudacor(comando, '\033[30;7m')
titulo('ATÉ LOGO!', '\033[41;1;30m')
