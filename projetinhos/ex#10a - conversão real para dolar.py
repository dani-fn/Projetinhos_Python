real = float(input('Quantos reais deseja converter?\n R$'))
dol = real / 5.34
if real <= 1:
    r1 = 'real vale'
else:
    r1 = 'Reais valem'
if dol <= 1:
    d1 = 'dólar'
else:
    d1 = 'dólares'
print('{} {} {:.2f} {}'.format(real, r1, dol, d1))
