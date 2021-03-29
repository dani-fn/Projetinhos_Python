from projetinhos.ex115.interface import *  # anotar isto: Para importar tudo
from projetinhos.ex115.arquivo import *
from time import sleep as s

cadastros = 'cadastros.txt'
if not arquivoexiste(cadastros):
    criararquivo(cadastros)
while True:
    opcao = menu(['Ver pessoas cadastradas',
                  'Cadastrar nova pessoa',
                  'Sair do Sistema'])
    s(0.8)
    if opcao == 1:
        titulo('PESSOAS CADASTRADAS')
        lerarquivo(cadastros)
    if opcao == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(cadastros, nome, idade)
    if opcao == 3:
        exit(titulo('Saindo do sistema... Até logo!'))


