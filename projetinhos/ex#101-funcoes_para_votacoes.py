def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO FACULTATIVO'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print()
nasc1 = int(input('Em que ano você nasceu? '))
print(voto(nasc1))
