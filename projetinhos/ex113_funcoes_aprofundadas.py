def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31;1mERRO! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31;1mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = str(input(msg)).strip().replace(',', '.')
            num = float(num)
        except (ValueError, TypeError):
            print('\033[31;1mERRO! Digite um número inteiro válido!\033[m')
            # consigo fazer sem o continue
        else:
            return num


i = leiaint('Digite valor inteiro: ')
r = leiafloat('Digite valor real:')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
