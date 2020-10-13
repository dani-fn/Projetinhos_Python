from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('\033[32m{} É UM ANO BISSEXTO!'.format(ano))
else:
    print('\033[32m{} NÃO É UM ANO BISSEXTO!'.format(ano))
