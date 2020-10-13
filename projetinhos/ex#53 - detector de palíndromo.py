frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper().split()
frase = ''.join(frase)
pali = ''

for letra in frase[::-1]:
    pali += letra

# for letra in range(len(frase) - 1, -1, -1):
#     pali += frase[letra]

print('O inverso de {} é {}'.format(frase, pali))
if pali == frase:
    print('A frase digitada \033[32;1mÉ UM PALÍNDROMO!')
else:
    print('A frase digitada \033[31;1mNÃO É UM PALÍNDROMO!')

# Tem como fazer esse exercício sem o "for":
# pali = frase[::-1]
