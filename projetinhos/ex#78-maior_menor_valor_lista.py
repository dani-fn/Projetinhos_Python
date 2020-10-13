valores = list()
posmaior = []
posmenor = []
for pos in range(0, 5):
    valores.append(eval(input(f'Digite um valor para a posição {pos}: ')))  # TODO o que é "eval"??
for key, valor in enumerate(valores):
    if max(valores) == valor:
        posmaior.append(key)
    if min(valores) == valor:
        posmenor.append(key)
print('-' * 48)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado é {max(valores)} na posição(ões) {posmaior}')
print(f'O menor valor digitado é {min(valores)} na posição(ões) {posmenor}')
