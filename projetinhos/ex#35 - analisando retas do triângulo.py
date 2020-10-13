print('\033[1;35m''='*48, '\033[m')
print('{:^48}'.format('\033[30;1mAnalisador de triângulos'))
print('\033[35;1m''='*48, '\033[m')
print('Me dê o comprimento de três retas e eu direi a você se\n é possível formar um triângulo com suas retas!')
a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta: '))
c = int(input('Digite o comprimento da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[1;32mSim!\033[30m é possível formar um triângulo com suas retas!')
else:
    print('\033[1;31mNão!\033[30m é IMpossível formar um triângulo!')
