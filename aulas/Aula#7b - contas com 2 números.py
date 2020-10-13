n1 = float(input('Digite um valor'))
n2 = float(input('Digite mais um valor'))
sm = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
mod = n1 % n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a potência é {}'.format(sm, m, e), end=' ')    # end= não ir p/ próxima linha
print('A subtração é {}, a divisão é {:.3f} \nA divisão inteira é {} e o resto ou módulo é {}'.format(sb, d, di, mod))
                                # :.3f para ter apenas e casas decimais (caracteres flutuantes)
                                            # \n ir para a próxima linha
                                            