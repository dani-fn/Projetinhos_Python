addidade = 0
agemolder = 0
namemolder = ''
f20count = 0
for pessoa in range(1, 5):
    print('='*5, '{}ª Pessoa'.format(pessoa), '='*5)
    nome = str(input('Nome: ')).strip
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if pessoa == 1 and sexo in 'mM':    # Também funciona assim pra não usar o .upper()
        agemolder = idade
        namemolder = nome
    addidade += idade
    if sexo == 'M' and agemolder < idade:
        agemolder = idade
        namemolder = nome
    elif sexo == 'F' and idade < 20:
        f20count += 1
medidade = addidade / 4
print('A média das idades é: ', medidade)
print('O homem mais velho tem {} anos e chama-se {}'.format(agemolder, namemolder))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(f20count))
