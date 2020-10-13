cont = 0
somidade = 0
mulheres = list()
todos = list()
while True:
    todos.append(dict())
    todos[cont]['nome'] = str(input('Nome: '))
    todos[cont]['sexo'] = str(input('Sexo: [M/F] '))[0]
    while todos[cont]['sexo'] not in 'mMfF':
        print('ERRO! Digite um valor válido!')
        todos[cont]['sexo'] = str(input('Sexo: [M/F] '))[0]
    if todos[cont]['sexo'] in 'fF':
        mulheres.append(todos[cont]['nome'])
    todos[cont]['idade'] = int(input('Idade: '))
    somidade += todos[cont]['idade']
    cont += 1
    mais = str(input('Quer continuar? [S/N] '))[0]
    while mais not in 'sSnN':
        print('ERRO! Digite um valor válido!')
        mais = str(input('Quer continuar? [S/N] '))[0]
    if mais in 'nN':
        break
print('-' * 30)
print(f'- O grupo tem {cont} pessoas')
media = somidade / cont
print(f'- A média de idade é de {media:.2f}')
print('- As mulheres cadastradas foram: ', end='')
for i, mulher in enumerate(mulheres):
    if i + 1 == len(mulheres):
        print(mulher)
    else:
        print(mulher, '/', end=' ')
print('\n- Quem está a cima da média:')
for k, acima in enumerate(todos):
    if todos[k]['idade'] > media:
        for i, v in todos[k].items():
            print(f'{i} = {v} ', end='')
        print()
print('<< ENCERRADO >>')
