n = float(input('Digite um valor númerico real'))
print(n)
print(type(n))

o = input('Digite algo')            #um 'INPUT' vai ser sempre STRING
print('isnumeric', o.isnumeric())   #isnumeric - é numerico?
print('isalpha', o.isalpha())       #isalpha - é letra? uma interface de números não é alpha
print('isalnum', o.isalnum())       #isalnum - é uma interface com alfabeto e número?
print('isupper', o.isupper())       #isupper - está somente com letras maiúsculas? ('islower()' também)
