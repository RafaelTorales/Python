'''n = int(input('Em qual número de 0 a 5 estou pensando? '))
print('Analisando...')
if n == 4:
    print('Parabéns você acertou!!')
else:
    print('Você errou!')'''
from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2.5)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
