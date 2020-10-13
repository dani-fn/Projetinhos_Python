soma = cont = n = 0
while n != 999:
    n = int(input('Digite um número: [999 PARA PARAR] '))
    if n != 999:
        soma += n
        cont += 1
print('foram digitados \033[35;1m{} números\033[m e a soma entre eles é de \033[32;1m{}'.format(cont, soma))
