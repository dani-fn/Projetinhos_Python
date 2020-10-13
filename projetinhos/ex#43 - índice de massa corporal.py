m = float(input('Qual o seu peso em kg? '))
h = float(input('Qual a sua altura em m? '))
imc = m / h**2
print('O seu IMC é {:.1f}, faixa de peso: '.format(imc), end='')
if imc <= 18.5:
    print('\033[33mAbaixo do peso\033[m - Cuidado, procure um \033[34mnutricionista')
elif imc < 25:
    print('\033[32mNormal\033[m - Parabéns!')
elif imc < 30:
    print('\033[33mSobrepeso\033[m - Cuidado')
elif imc < 40:
    print('\033[33mObesidade\033[m - Cuidado! Procure um \033[34mnutricionista')
else:
    print('\033[31mObesidade mórbida - Procure um médico com \033[31;1murgência!')
