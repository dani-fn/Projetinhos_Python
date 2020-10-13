def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: (optional) deve ou não adicionar a situação da turma
    :return: dicionário com informações e situação da turma
    """
    cont = 0
    d = dict()
    mai = men = int()
    soma = int()
    for nota in n:
        cont += 1
        soma += nota
        if cont == 1:
            mai = nota
            men = nota
        elif nota > mai:
            mai = nota
        elif nota < men:
            men = nota
    d['total'] = cont
    d['maior nota'] = mai
    d['menor nota'] = men
    d['média'] = soma / cont    # mais fácil: sum(n) / len(n)
    if sit:
        if d['média'] < 5:
            d['situação'] = 'RUIM'
        elif d['média'] < 7:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'BOA'
    return d


analise = notas(7, 7, 9, sit=True)
print(analise)
help(notas)
