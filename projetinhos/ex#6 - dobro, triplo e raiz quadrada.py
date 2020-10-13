print('Me de um valor e eu te darei o seu dobro, triplo e sua raiz quadrada')
n = int(input('Digite um número'))
dob = n * 2
tri = n * 3
sr = pow(n, (1/2))
print('O dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {:.6f}'.format(n, dob, n, tri, n, sr))
