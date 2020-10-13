dist = float(input('Quantos quilômetros você deseja viajar?'))
if dist < 200:
    p = dist * 0.50
else:
    p = dist * 0.45
# preço = dist * 0.50 if dist < 200 else dist * 0.45 (outra forma de fazer)
print('O preço da passagem será de \033[32mR${:.2f}'.format(p))
