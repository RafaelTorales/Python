from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('\033[1;34;30m+§\033[m' * 20)
print('\033[1;34m               VAMOS JOGAR!\033[m')
print('\033[1;34;30m+§\033[m' * 20)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format((itens[jogador])))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
