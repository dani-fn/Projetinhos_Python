nome = str(input('Digite o seu nome completo: ')).strip()
print('Muito prazer em te conhecer!')
div = nome.split()
print('Seu primeiro nome é {}'.format(div[0]))
print('Seu último nome é {}'.format(div[len(div)-1]))
