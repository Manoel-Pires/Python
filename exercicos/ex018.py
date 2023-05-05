from math import sin, cos,tan, radians
an = float(input('digite o angulo:'))
seno = sin(radians(an))
cosseno = cos(radians(an))
tg = tan(radians(an))
print('o angulo {} tem o seno de {:.2f}' .format(an, seno))
print('o cosseno é de {:.2f}' .format(cosseno))
print('a tangente vale {:.2f}' .format(tg))
