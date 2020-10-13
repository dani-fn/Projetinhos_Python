def leiaint(msg):
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print('\033[31;1mERRO! Digite um número inteiro válido!\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
