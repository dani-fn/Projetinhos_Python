n = s = 0
while True:         # Flag é o ponto de parada (999 nesse caso)
    n = int(input('Digite um número [999 p/ sair]: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')
