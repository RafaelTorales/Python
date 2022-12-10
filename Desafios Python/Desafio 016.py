'''from math import trunc
#a = float(input('Digite seu número com virgula: '))
#b = math.trunc(a)
#print('O seu número inteiro fica {}'.format(b))
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''
num = float(input('Digite um valor: '))
print('O valor digitado foi {}  e a sua porção inteira é {:.0f}'.format(num, num))
