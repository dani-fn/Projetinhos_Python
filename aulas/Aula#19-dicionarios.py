# adicionar "as" na aula de módulos

#Três tipos de variáveis compostas:
#   tuplas
#   listas
#   dicionários

# dados = dict()
# dados = {}

dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'     # ADICIONADO (não tem append)

del dados['idade']

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }

print(filme.values())           # Pega só o valor que foi designado as keys

print(filme.keys())             # Pega só as keys

print(filme.items())            # Pega os dois juntos, representa cada item por tuplas

print()

for k, v in filme.items():      # IMPORTANTE, não existe "enumerate", diferente das tuplas e listas
    print(f'O {k} é {v}')

for k in filme.keys():
    print(k)

locadora = [[{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}],
            [{'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}],
            [{'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}]]

# print(locadora[0]['titulo']) #  pq eu não consigo?   R: ver na Aula#19a
