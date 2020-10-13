print('4 ao cubo como "4**3" =', 4**3)
print('agora como "pow(4, 3)" =', pow(4, 3))

#a raiz quadrada é escrita elevando o radicando por (1/2), já a cúbica, (1/3)

print('raiz quadrada de 81: {} ='.format('81**(1/2)'), 81**(1/2))
print('raiz cúbica de 125: {} ='.format('125**(1/3)'), 125**(1/3))

print('Oi'*8)
print('='*5)

nome = input('Qual é o seu nome?')
print('Prazer em te conhecer, {:20}!'.format(nome))     # ":20" faz ocupar 20 caracteres
print('Prazer em te conhecer, {:>15}!'.format(nome))    # ":>15" faz a mesma coisa, só que deixa alinhado à direita
print('Prazer em te conhecer, {:^30}!'.format(nome))    # ":^30" Centralizado
print('Prazer em te conhecer, {:=^40}!'.format(nome))   # ":=" coloca o símbolo ao redor
