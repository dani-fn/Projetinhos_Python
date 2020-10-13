from math import hypot
print('Vou calcular o comprimento de qualquer hipotenusa para você!')
cat1 = float(input('comprimento do cateto adjacente: '))
cat2 = float(input('comprimento do cateto oposto: '))
h = hypot(cat1, cat2)
print('a hipotenusa é {}'.format(h))
