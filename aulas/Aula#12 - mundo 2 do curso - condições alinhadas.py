# if:
#    bloco 1
# elif:
#    bloco 2
# elif:
#    bloco 3
# else:
#    bloco 4

nome = str(input('Qual é o seu nome? '))
if nome == 'Daniel':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular!')
elif nome in 'Giovanna Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem "Meh..."')
print('Tenha um bom dia {}'.format(nome))
