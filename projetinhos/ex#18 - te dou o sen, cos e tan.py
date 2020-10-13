from math import sin, cos, tan, radians
print('Me dê um ângulo e eu te darei seu seno, cosseno e tangente!')
ang = float(input('Digite o ângulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('{} tem:\nseno:       {:.2f}\ncosseno:    {:.2f}\ntangente:   {:.2f}'.format(ang, seno, cosseno, tangente))
