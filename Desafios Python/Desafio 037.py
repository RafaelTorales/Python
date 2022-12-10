num = int(input('Escolha um número para converter: '))
print('''Escolha uma das bases para conversão:
[ 1 ] para converter para \033[1;34mBINÁRIO\033[m
[ 2 ] para converter para \033[1;34mOCTAL\033[m
[ 3 ] para converter para \033[1;34mHEXADECIMAL\033[m''')
base = int(input('Qual sua opção? '))
if base == 1:
    print('O número em base binária é \033[1;34m{}\033[m'.format(bin(num)[2:]))
    print('Número convertido com sucesso!')
elif base == 2:
    print('O número em base octal é \033[1;34m{}\033[m'.format(oct(num)[2:]))
    print('Número convertido com sucesso!')
elif base == 3:
    print('O número em base hexadecimal é \033[1;34m{}\033[m'.format(hex(num)[2:]))
    print('Número convertido com sucesso!')
else:
    print('\033[4;31mOpção inexistente')
