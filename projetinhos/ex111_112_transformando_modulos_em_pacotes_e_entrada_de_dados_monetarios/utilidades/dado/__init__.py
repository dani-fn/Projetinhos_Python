def leiadinheiro(msg):
    while True:
        num = str(input(msg)).replace(',', '.').strip()
        if '.' in num or num.isnumeric():
            return float(num)
        else:
            print(f'\033[31;1mERRO! \"{num}\" é um preço inválido\033[m')  # O que essa barra invertida faz???
