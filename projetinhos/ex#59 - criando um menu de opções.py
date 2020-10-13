from time import sleep
n1 = float(input('\033[33mPrimeiro valor: '))
n2 = float(input('Segundo valor: '))
aberto = True
maior = 0
while aberto is True:
    print('\033[30m[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior valor\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa')                                      # O que ctrl + shift + up/down faz?
    opcao = int(input('\033[mQual sua opção? '))
    if opcao == 1:
        print('\033[32;1m{} + {} = {}\033[m'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('\033[32;1m{} x {} = {}\033[m'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 != n2:
            if n1 < n2:
                maior = n2
            elif n2 < n1:
                maior = n1
            print('\033[32;1m{} é o maior número\033[m'.format(maior))
        else:
            print('\033[32;1mOs dois números são equivalentes\033[m')
    elif opcao == 4:
        n1 = float(input('\033[33mDigite o primeiro número: '))
        n2 = float(input('Digite o segundo número: \033[m'))
    elif opcao == 5:
        print('\033[35;1mObrigado! Volte sempre!\033[m')
        aberto = False
    else:
        print('\033[31;1mOpção inválida!\033[m')
    sleep(1)
