sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    novo = sal + (15 / 100 * sal)
else:
    novo = sal * 1.10
print('\033[30mQuem ganhava \033[1;31mR${:.2f}\033[30m passa a ganhar \033[1;32mR${:.2f}\033[30m agora.'.format(sal, novo))
