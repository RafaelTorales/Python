def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    tam = len(num)
    mai = 0
    for n in num:
        print(f'{n} ', end='')
        if num == 0:
            mai = n
        if n > mai:
            mai = n
        sleep(0.3)
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


#Programa Principal
from time import sleep

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
