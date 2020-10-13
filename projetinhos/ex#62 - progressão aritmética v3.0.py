print('*' * 15)
print('GERADOR DE P.A')
print('*' * 15)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
c = 1
add = 1
while add != 0:
    while c <= 10:
        print(a1, ' ► ' if c < 10 else '', end='')
        c += 1
        a1 += r
    add = int(input('\nQuantos termos você quer mostrar a mais? '))
    term = c + add - 1
    while c <= term:
        print(a1, ' ► ' if c < term else '', end='')
        c += 1
        a1 += r
print('Exercício finalizado com {} termos a mostra'.format(c-1))
print('Obrigado!')
