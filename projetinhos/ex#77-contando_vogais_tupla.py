palavras = ('chocolate', 'banana', 'comida', 'amor', 'lutar',
            'cantar', 'viver', 'construir', 'musica', 'saxofone')
for word in palavras:          # todo O que é lambda??
    print(f'\nNa palavra {word.upper()} temos: ', end='')
    for letra in word:   # e se eu usar "pos"
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
