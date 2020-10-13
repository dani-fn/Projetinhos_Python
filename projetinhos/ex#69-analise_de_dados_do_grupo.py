totmaior = tothomem = tot20f = 0
while True:
    print('-'*24)
    print('{:^24}'.format('CADASTRE UMA PESSOA'))
    print('-'*24)
    sexo = parar = '.'
    idade = int(input('Idade: '))
    # try:
    #     idade = int(idade)            # TODO o que é tudo isso? (try)
    # except ValueError:
    #     print("That's not an int!")
    while sexo not in 'mMfF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    if idade >= 18:
        totmaior += 1
    if sexo in 'mM':                # Tem SIM diferença entre if e elif, com o if: pode ser os dois
        tothomem += 1               # .                                com o elif: é só um dos dois
    if sexo in 'fF' and idade < 20:
        tot20f += 1
    while parar not in 'sSnN':
        parar = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if parar in 'nN':
        print('{:+^40}'.format(' FIM DO PROGRAMA '))
        break
print(f'Total de {totmaior} pessoas maiores de idade')
print(f'Ao todo, foram {tothomem} homem(ns) cadastrados')
print(f'E {tot20f} mulher(es) com menos de 20 anos cadastradas')
