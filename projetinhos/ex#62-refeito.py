print('-'*15)
print('Gerador de P.A')
print('-'*15)
a1 = int(input('Digite o primeiro valor: '))
r = int(input('Digite a razão da P.A: '))
term = a1
cont = 1
total = 0
add = 10
while add != 0:
    total = total + add
    while cont <= total:
        print(term, ' ► ' if cont < total else '', end='')
        cont += 1
        term += r
    add = int(input('\nQuantos mais termos você quer ver? '))
print(f'Exercício finalizado com {total} termos a mostra')
print('Obrigado!')
