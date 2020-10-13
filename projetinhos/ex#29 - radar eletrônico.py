v = float(input('Qual a velocidade do seu carro em km/h?'))
if v > 80:
    p = (v - 80) * 7
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você deve pagar uma multa de \033[1;31mR${:.2f}\033[m'.format(p))
print('Tenha um bom dia! Dirija com segurança!')
