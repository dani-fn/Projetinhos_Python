from aulas.Aula23_modulos_e_pacotes.uteis import numeros

num = int(input('Digite um número: '))
fat = numeros.fatorial(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
