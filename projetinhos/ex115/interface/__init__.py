def linha(tam=48):
    return '-' * tam


def titulo(msg):
    print(linha())
    print(f'{msg}'.center(48))
    print(linha())


def leiaop(msg, a, b):
    erro = '\033[31m ERRO! Digite uma opção válida!\033[m'
    while True:
        try:
            v = int(input(msg))
        except (TypeError, ValueError):
            print(erro)
            continue
        except KeyboardInterrupt:
            print('\033[31;1mEntrada de dados interrompida pelo usuário\033[m')
            exit()
        else:
            if a <= v < b:
                return v
            else:
                print(erro)


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    return leiaop('\033[32m Sua opção: \033[m', 1, len(lista)+1)


def leiaint(prompt):
    erro = '\033[31m ERRO! Digite uma opção válida!\033[m'
    while True:
        try:
            v = int(input(prompt))
        except (TypeError, ValueError):
            print(erro)
            continue
        except KeyboardInterrupt:
            print('\033[31;1mEntrada de dados interrompida pelo usuário\033[m')
            exit()
        else:
            return v
