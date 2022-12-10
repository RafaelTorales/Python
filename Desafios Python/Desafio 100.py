from random import randint
from time import sleep


def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        a = randint(0, 10)
        print(f'{a} ', end='')
        numeros.append(a)
        sleep(0.4)
    print('PRONTO!')


def somapar():
    par = 0
    for n in numeros:
        if n % 2 == 0:
            par += n
    print(f'Somando os valores pares de {numeros}, temos {par}')


numeros = list()
sorteia()
somapar()
