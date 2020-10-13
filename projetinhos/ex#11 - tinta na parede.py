print('Quantas latas de tinta vamos precisar pra pintar a sua parede? cada lata rende 2m²')
L = float(input('Qual a largura da parede, em metros? '))
H = float(input('Qual a altura da parede, em metros? '))
A = L * H
t = A // 2
if t is 1:
    lata = 'lata'
else:
    lata = 'latas'
print('Você irá precisar de {} {} de tinta'.format(t, lata))
