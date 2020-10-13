nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é: \033[30m', nome.upper(), '\033[m')
print('Seu nome em minúsculas é: {}{}{}'.format('\033[30m', nome.lower(), '\033[m'))
dividido = nome.split()
print('Seu nome tem ao todo, \033[1;30m{}\033[m letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é \033[7;30m{}\033[m e ele tem \033[30;1m{}\033[m letras'
      .format(dividido[0], len(dividido[0])))
# também serve: nome.find(' ') achando o primeiro espaço
