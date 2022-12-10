'''a = float(input('Quanto mede o cateto que está em pé: '))
b = float(input('Quanto mede o cateto que está deitado: '))
c = (a ** 2 + b ** 2) ** (1/2)
print('O valor da hipotenusa é: {:.2f}!'.format(c))'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
