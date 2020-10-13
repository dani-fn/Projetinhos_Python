expressao = str(input('Digite a expressão (com parênteses): '))
pilha = []
for carac in expressao:
    if carac == '(':
        pilha.append('(')
    elif carac == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
