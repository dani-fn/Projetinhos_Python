nome = str(input('Qual é o seu nome?'))
if nome == 'Daniel':
    print('Que nome lindo você tem!')
print('Bom dia {} '.format(nome))           # Não precisou do "ELSE" (estrutura condicional simples)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim!')

print('Parabéns' if m >= 6 else 'ESTUDE MAIS!')
