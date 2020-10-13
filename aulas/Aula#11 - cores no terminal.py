
# O código é:
#               /033[a;b;cm     sendo abc os números
# Sobre os 3 números dps do "[", na ordem:
#       STYLE:  0 None - 1 Bold - 4 Underline - 7 Negative
#       TEXT:   30 - 31 - 32 - ... - 37       (cada número é uma cor)
#       BACK:   40 - 41 - 42 - ... - 47

print('\033[30;41mteste')
print('\033[4;44;33mteste\033[m')        # a ordem dos números não importa
print('\033[1;35;43mteste\033[m')
print('\033[0;30;42mteste\033[m')
print('\33[mteste\33[m')                      # padrão
print('\33[7;30mteste\33[m')                  # diferença colocando o "ZERO" ou não?

print('\033[1;30;45m Olá Daniel! \033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Daniel'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;32m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
