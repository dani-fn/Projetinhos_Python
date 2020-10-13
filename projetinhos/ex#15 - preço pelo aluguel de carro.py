print('Veremos o preço a ser pago pelo aluguel')
d = int(input('Você ficou com o carro por quantos dias? '))
km = float(input('Quantos km você viajou? '))
p = d * 60 + km * 0.15
print('Aluguel no valor de R${:.2f}'.format(p))
