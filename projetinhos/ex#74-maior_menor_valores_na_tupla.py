from random import randint
n1 = randint(0, 10)
maior = menor = n1
n2 = randint(0, 10)
if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2
n3 = randint(0, 10)
if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3
n4 = randint(0, 10)
if n4 > maior:
    maior = n4
elif n4 < menor:
    menor = n4
n5 = randint(0, 10)
if n5 > maior:
    maior = n5
elif n5 < menor:
    menor = n5
tupla = (n1, n2, n3, n4, n5)
print(f'A tupla é: {tupla}')
print(f'O menor valor é {menor} e o maior valor é {maior}')
