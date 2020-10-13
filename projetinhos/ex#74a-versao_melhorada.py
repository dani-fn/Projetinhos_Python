from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))
print('Os números sorteados foram:', end='')
for num in tupla:
    print(f' {num} ', end='')
print(f'\nO maior número é {max(tupla)}')
print(f'O menor número é {min(tupla)}')
