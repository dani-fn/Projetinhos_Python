a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos podem formar um triângulo', end=' ')
    if a == b == c:
        print('\033[32mEQUILÁTERO')
    elif a == b or a == c or b == c:
        print('\033[32mISÓSCELES')
    else:
        print('\033[32mESCALENO')
else:
    print('\033[31;1mNÃO\033[31m é possível formar um Triângulo!')
