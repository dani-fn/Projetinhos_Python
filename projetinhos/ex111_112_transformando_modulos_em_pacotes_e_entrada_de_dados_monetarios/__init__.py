from projetinhos.ex111_112_transformando_modulos_em_pacotes_e_entrada_de_dados_monetarios.utilidades import moeda
from projetinhos.ex111_112_transformando_modulos_em_pacotes_e_entrada_de_dados_monetarios.utilidades import dado

p = dado.leiadinheiro('Digite um preço: R$')
moeda.resumo(p, 80, 35)
