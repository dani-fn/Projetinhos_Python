aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] > 6:
    aluno['Situação do aluno'] = 'Aprovado'
else:
    aluno['Situação do aluno'] = 'REPROVADO'
for k, v in aluno.items():
    print(k, ':', v)
