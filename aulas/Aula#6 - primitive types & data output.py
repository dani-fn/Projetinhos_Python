n1=int(input('Digite um número'))
n2=int(input('Digite mais um número'))
s=n1+n2
#print('A soma entre', n1, 'e', n2, 'é', s)     ou melhor...
print('A soma entre {} e {} vale {}').format(n1, n2, s)

#int(input('"int" para número inteiro'))
#float(input('"float" para números reais como -15.223 ou 0.0'))
#bool(input('"bool" para um valor booleano(ou valor lógico) podendo ser "True" ou "False"'))
#str(input('"str" para uma interface, como "7.5" ou ""(interface vazia)'))

#posso usar Hashtags para criar anotações!

print('A soma vale',s)
    #maneira melhor de escrever:
print('A some vale {}'.format(s))
