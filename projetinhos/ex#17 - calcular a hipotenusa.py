from math import pow, sqrt
print('Vou calcular o comprimento de qualquer hipotenusa para você!')
cat1 = float(input('comprimento do cateto adjacente: '))
cat2 = float(input('comprimento do cateto oposto: '))
h = sqrt((pow(cat1, 2) + pow(cat2, 2)))
print('a hipotenusa é {}'.format(h))
