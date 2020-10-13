sexo = str(input('Qual o seu sexo[M/F]? ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[31;1mInsira um sexo válido!\033[m\nQual o seu sexo[M/F]? ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo masculino registrado, Obrigado')
else:
    print('Sexo feminino registrado, Obrigado')
