pessoas = {'nome': 'Daniel', 'sexo': 'M', 'idade': 20}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# Na hora de referenciar os elementos, eu uso colchetes
# Na hora de declarar, eu uso chaves

print()

estado = {}
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # Não vou conseguir dar brasil.append(estado[:]) pq estado é um dicionário. Então...
    brasil.append(estado.copy())

for estado in brasil:
    for v in estado.values():
        print(v, end=' ')
