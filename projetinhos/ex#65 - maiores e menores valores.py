continuar = 'S'
soma = quant = 0
n = int(input('Digite um número: '))
maior = menor = n                       # Também posso usar "if quant == 1:" dentro do while
while continuar in 'Ss':
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
    quant += 1
    continuar = str(input('Quer continuar?[S/N] ')).strip().upper()
    if continuar not in 'SN':
        print('Digite uma resposta válida!')
        continuar = str(input('Quer continuar?[S/N] ')).strip().upper()
    elif continuar in 'Ss':
        n = int(input('Digite um número: '))
media = soma / quant
print('A \033[35;1mmédia\033[m dos {} números digitados é \033[32;1m{}'.format(quant, media))
print('O \033[33;1mMENOR valor foi {}\033[m e o \033[34;1mMAIOR valor foi {}'. format(menor, maior))
