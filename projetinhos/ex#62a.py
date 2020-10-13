print('-'*15)
print('Gerador de P.A')
print('-'*15)
a1 = int(input('Digite o primeiro valor: '))
r = int(input('Digite a razão da P.A: '))
term = a1
cont = 1
add = 10
total = 0
while add != 0:
    total = total + add
    while cont <= total:
        print(term, ' ► ' if cont < total else '', end='')
        term += r
        cont += 1
    add = int(input('\nQuer mostrar mais quantos termos? '))
print('P.A encerrada. Foram gerados {} termos.'.format(total))
print('Obrigado!')
