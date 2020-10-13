dados = list()
dados.append('pedro')
dados.append(25)
pessoas = list()
                                # se não usar [:], eu vou criar uma ligação entre as listas
pessoas.append(dados[:])        # [:] para uma cópia de dados
print(pessoas)                  # Dentro da lista, eu tenho outra lista
#                 0             1               2
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])    # Só 'Pedro'
print(pessoas[2][1])    # 32
print(pessoas[1])       # ['Maria', 19]

galera = [['João', 19], ['Ana', 33],
          ['Joaquim', 13], ['Maria', 45]]
print(galera)
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
