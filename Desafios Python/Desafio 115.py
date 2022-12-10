from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

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
