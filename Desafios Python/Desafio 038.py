a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
if a > b:
    print('O \033[1;33mprimeiro valor\033[m é \033[1;34mmaior!\033[m')
elif b > a:
    print('O \033[1;33msegundo valor\033[m é \033[1;34mmaior!\033[m')
else:
    print('\033[1;33mNão existe\033[m valor maior, os dois são \033[1;34miguais!\033[m')
