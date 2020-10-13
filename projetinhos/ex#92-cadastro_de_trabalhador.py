from datetime import date
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Em que ano você nasceu? '))
cadastro['Idade'] = date.today().year - nasc
cadastro['CTPS'] = int(input('Carteira de trabalho: (0 = não tem) '))
if cadastro['CTPS'] > 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: R$'))
    # trabalhado = date.today().year - cadastro['contratação']
    # idadeinicio = cadastro['idade'] - trabalhado
    # cadastro['aposentadoria'] = idadeinicio + 35
    cadastro['Aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - date.today().year)
print('-=-' * 10)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
