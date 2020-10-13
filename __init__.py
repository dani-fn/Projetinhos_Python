def arquivoexiste(nome):
    try:
        testar = open(nome, 'rt')
        testar.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    criando = open(nome, 'wt+')
    criando.close()
    print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    arquivo = open(nome, 'rt')
    for linha in arquivo:
        dado = linha.split(';')  # dividir no ponto e virgula existente
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')
    arquivo.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
