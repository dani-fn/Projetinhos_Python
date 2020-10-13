ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    print('O ano atual é bissexto!')
else:
    if ano % 400 == 0:
        print('{} é um ano bissexto!'.format(ano))
    else:
        if ano % 100 == 0:
            print('{} não é um ano bissexto!'.format(ano))
        else:
            if ano % 4 == 0:
                print('{} é um ano bissexto!'.format(ano))
            else:
                print('{} não é um ano bissexto!'.format(ano))
