# esse exercício ainda não pode ser feito da maneira de STRING
# temos que fazê-lo da maneira MATEMÁTICA
num = int(input('Informe um número de 0 a 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

# Se eu dividir qualquer número inteiro por 10, o seu módulo será igual ao último algarismo
# Fazendo ma divisão inteira por 10, é eliminado o último algarismo!
