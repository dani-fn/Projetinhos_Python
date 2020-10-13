pares = 0
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Digite um último número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if numeros.count(3) == 0:
    print('O valor 3 não foi digitado')
else:                                                       # Ou "if 3 in numeros:
    print(f'O valor 3 apareceu em {numeros.index(3)+1}º')
# for n in numeros:
#     if n % 2 == 0:
#         pares += 1
# if pares > 0:
#     print('O(s) valor(es) par(es): ', end='')
#     for n in numeros:
#         if n % 2 == 0:
#             print(n, end=' ')
print('O(s) valor(es) par(es): ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
        pares += 1
if pares == 0:
    print('Nenhum')
