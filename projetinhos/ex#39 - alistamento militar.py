from datetime import date
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
if idade < 18:
    if idade == 17:
        psfalta = 'Falta'
        psano = 'ano'
    else:
        psfalta = 'Faltam'
        psano = 'anos'
    print('Ainda não chegou a sua hora, futuro recruta!')
    print('{} {} {} para você se alistar!'.format(psfalta, 18 - idade, psano))
elif idade == 18:
    print('ESTÁ NA HORA! Você deve se alistar IMEDIATAMENTE!')
else:
    passou = idade - 18
    if passou == 1:
        psano = 'ano'
    else:
        psano = 'anos'
    print('Você já deveria ter se alistado há {} {}'.format(passou, psano))
