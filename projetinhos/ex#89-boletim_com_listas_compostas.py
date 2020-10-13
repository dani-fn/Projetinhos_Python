from time import sleep
lista = []
aluno = list()
notas = list()
while True:
    aluno.append(str(input('Nome: ')))
    notas.append(float(input('Primeira nota: ')))
    notas.append(float(input('Segunda nota: ')))
    aluno.append(notas[:])
    lista.append(aluno[:])                      # Também dá: ficha.append([nome, [nota1, nota2], media])
    aluno.clear()
    notas.clear()
    mais = str(input('Quer continuar? [S/N] '))[0]
    if mais not in 'Ss':
        break
print('-=' * 16)
print(f'{"No.":<3} {"NOME":<16} {"MÉDIA"}')
print('-' * 28)
for i, aluno in enumerate(lista):
    print(f'{i:<3} {lista[i][0]:.<16} {(lista[i][1][0]+lista[i][1][1]) / 2:.1f}')
while True:
    print('-=' * 16)
    num = int(input('Mostrar a nota de qual aluno? (999 interrompe): '))
    if num == 999:
        break
    if num <= len(lista) - 1:
        print(f'As notas de {lista[num][0]} são {lista[num][1]}')
print('FINALIZANDO', end='')
for ponto in range(0, 3):
    sleep(0.3)
    print('.', end='')
print()
print(f'\n{"  Volte Sempre!  ":+^21}')
