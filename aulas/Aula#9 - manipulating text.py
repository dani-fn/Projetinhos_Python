frase = 'Curso em Vídeo Python'  # 'n' é o 20º caractere
#print('C 0\nu 1\nr 2\ns 3\no 4\n  5\ne 6\nm 7\n  8\nV 9\ní 10\nd 11\ne 12\no 13\n  14\nP 15\ny 16\nt 17\nh 18\no 19\nn 20')
print('{:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2}'.format('C','u','r','s','o',' ','e','m',' ','V','i','d','e','o',' ','P','y','t','h','o','n'))
print('{:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {} {} {} {} {} {} {} {} {} {} {}'.format(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

print('{:=^48}'.format('Fatiamento'))

print('frase[9] = ', frase[9])                                # Print no nono caractere
print('frase[9:13] = ', frase[9:13])                          # O 13º ('o') fica de fora
print('frase[9:21] = ', frase[9:21])                          # Vai pegar a frase toda apesar de só ir até o 20
print('frase[9:21:2] = ', frase[9:21:2])                      # Vai pulando de 2 em 2
print('frase[:5] = ', frase[:5])                              # Vai do ZERO até o quinto
print('frase[15:] = ', frase[15:])                            # Vai do 15º até o final (no caso, é melhor do que ter usado o ':21'
print('frase[9::3] = ', frase[9::3])                          # Vai até o final, só que pulando de 3 em 3

print('{:=^48}'.format('Análise'))

print('len(frase) = ', len(frase))                            # Quantos caracteres a frase tem
print('frase.count("o") = ', frase.count('o'))                # Quantos 'o's (mínusculos) tem
print('frase.count("o", 0, 13) = ', frase.count('o', 0, 13))  # Quantos 'o's ATÉ o 13º caractere
print('frase.find("deo") = ', frase.find('deo'))              # Acha e mostra a posição dos caracteres na frase     # Tambem tem o ".rfind", que procura da direita p/ esquerda
print('frase.find("Android") = ', frase.find('Android'))      # Ele mostra um "-1" quando não encontra nada
print('"Curso" in frase = ', 'Curso' in frase)                # Isso é um OPERADOR (mostra True ou False)

print('{:=^48}'.format('Transformação'))

print('frase.replace()', frase.replace('Python', 'Android'))  # Substitui os caracteres por outro
print('frase.upper()', frase.upper())                         # Transforma para UPPER
print('frase.lower()', frase.lower())                         # Transforma para LOWER
print('frase.capitalize()', frase.capitalize())               # Tudo fica LOWER mas e o primeiro caractere fica UPPER
print('frase.title()', frase.title())                         # Ele identifica os 'SPACES' e coloca as primeiras letras UPPER
print('')
print('frase = "   Aprenda Python   " (com espaços)')
frase = '   Aprenda Python   '
print('frase.strip()', frase.strip())                         # Remove os SPACES antes e depois da str
print('frase.rstrip()', frase.rstrip())                       # Remove os últimos SPACES
print('frase.lstrip()', frase.lstrip())                       # Remove os primeiros SPACES

print('{:=^48}'.format('Divisão'))

frase = 'Curso em Vídeo Python'
print('frase.split()', frase.split())                         # Promove nova indexação p/ cada palavra, divide em palavra 0, 1, 2, 3,...

print('{:=^48}'.format('Junção'))

print('"".join(frase)', ''.join(frase))                       # junta os elementos, gerando uma única interface
print('"-".join(frase)', '-'.join(frase))                     # junta os elementos, gerando uma única interface, colocando o caractere escolhido
                                                              # TODO: estranho ele colocar entre as letras
print('-' * 48)

print('print("""interface""") para dar print em um texto grande')
print('exemplo:')
print("""Welcome to PyCharm help!

PyCharm is a dedicated Python and Django IDE providing a wide
range of essential tools for Python developers, tightly integrated
together to create a convenient environment for productive Python
development and Web development.""")
