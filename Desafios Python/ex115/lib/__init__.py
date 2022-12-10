from interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cavecalho('Opção 1')
    elif resposta == 2:
        cavecalho('Opção 2')
    elif resposta == 3:
        cavecalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
