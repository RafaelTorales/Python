'''from random import randint
from time import sleep
computador = randint(0, 10) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre \033[1;34m0\033[m e \033[1;34m10\033[m. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? ')) #Jogador tenta adivinhar
print('\033[36mPROCESSANDO...\033[m')
sleep(1)
cont = 1
while jogador != computador:
    print('\033[31mTente novamente!\033[m')
    jogador = int(input('Em qual número eu pensei? '))
    print('\033[36mPROCESSANDO...\033[m')
    sleep(1)
    cont = cont + 1
print('\033[1;32mVocê acertou!\033[m E precisou de \033[34m{}\033[m tentativas!'.format(cont))'''
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um númeor entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))