a = (5, 2, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)    # A + B != de B + A

print(c.count(5))

print(c.index(2, 4))    # Começando da posição 4 (chama-se deslocamento)

pessoa = ('Daniel', 19, 'M', 75.0)  # Posso sim misturar os tipos
del pessoa  # É imutável, podemos APENAS apagá-la
