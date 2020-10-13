while True:
    print('-'*59)
    n = int(input('Quer ver a tabuada de qual valor?(número negativo p/ parar) '))
    print('-'*59)
    if n < 0:
        break
    for tab in range(1, 11):
        print(f'{n} x {tab:<2} = {n*tab}')
print('Programa tabuada-v3.0 encerrado.')
