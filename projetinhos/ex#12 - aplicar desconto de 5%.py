print('vou calcular o seu desconto de %5 para o valor de qualquer item.')
p = float(input('Qual o valor, em reais, que vamos trabalhar? '))
d = p * 0.95  # também serve d = p - (p*5/100)
if d <= 1:
    r = 'real'
else:
    r = 'reais'
print('O valor com o desconto será de {} {}'.format(d, r))
