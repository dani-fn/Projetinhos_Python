lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[2] = 'sorvete'                    # São MUTÁVEIS
print(lanche)
lanche.append('cookie')                  # Adiciona no final
print(lanche)
lanche.insert(0, 'hot dog')              # Adiciona onde eu quiser, sem tirar nada
print(lanche)
del(lanche[0])  # ou lanche.pop(0)       # pop() tira o ÚLTIMO
print(lanche)
lanche.remove('cookie')                  # removo determinado valor (sem colocar o índice)
print(lanche)
if 'pizza' in lanche:
    lanche.remove('pizza')               #todo o que faz o comando "pass"

valores1 = list(range(4, 11, 2))         # outra forma de criar uma lista
print(valores1)
valores2 = [5, 2, 7, 6, 8, 1, 9]         # Sem ordem
print(valores2)
print(valores2[3])  # → 6
valores2.sort()                          # Organizar em ordem
print(valores2)
valores2.sort(reverse=True)              # Organizar ao inverso
print(valores2)
print('-' * 32)
print(f'Essa lista tem {len(valores2)} elementos')          # podemos usar o "len"

valores2.insert(5, 8)                    # pos 5 valor 8
print(valores2)
valores2.remove(8)                       # Tirou só o primeiro "8"
print(valores2)
