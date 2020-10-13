frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))     # Antes não tinha nenhum O maiúsculo, mas com a combinação feita, tem!
print(len(frase))
print(frase[0])
print(frase.replace('Python', 'Daniel'))
print(frase)  # Não contou o 'Daniel' da linha anterior!
frase = frase.replace('Python', 'Daniel')
print(frase)    # AGORA FOI, pq eu salvei na linha anterior!
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('curso'))
print(frase.lower().find('curso'))
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[2])      # Mostra a segunda parte do que foi dividido
print(dividido[2][3])   # Mostra o caractere 3 da segunda parte
