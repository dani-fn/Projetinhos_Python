print('Ajuste de 15% do salário')
s = float(input('Digite seu salário: '))
a = s * 1.15        # ou a = s + (s * 15/100)
if a <= 1:
    r = 'real'
else:
    r = 'reais'
print('Seu novo salário é de {:.2f} {}!'.format(a, r))
