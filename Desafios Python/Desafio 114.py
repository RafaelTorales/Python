import urllib.request
try:
    urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[0;32mConsegui acessar o site Pudim com sucesso!\033[m')
