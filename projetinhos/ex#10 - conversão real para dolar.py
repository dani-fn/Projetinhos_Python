real = float(input('Quantos reais deseja converter?\n R$'))
dol = real / 5.34
if real > 1 and dol > 1:
    print('{} reais valem {} dólares'.format(real, dol))    # esse espaço antes do print chama INDENTAÇÃO
if real <= 1 and dol <= 1:
    print('{} real vale {} dólar'.format(real, dol))
if real > 1 and dol <= 1:
    print('{} reais valem {} dólar'.format(real, dol))
