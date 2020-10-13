# Laço com variável de controle

# for c in range(0, 3):
#     if moeda:
#         pega
#     print('passo')
#     print('pula')
# print('passo')
# print('pega')

for c in range(6, 0, -1):
    print(c)
print('FIM')

for c in range(0, 9, 2):
    print(c)
print('FIM')

#  ==================================================

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for soma in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print('A somatória dos números é: {}'.format(s))
