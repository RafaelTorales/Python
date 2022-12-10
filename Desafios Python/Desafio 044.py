print('\033[1;32m{:-^40}\033[m'.format('LOJAS RAFINHA'))
valor = float(input('Qual o valor do produto? R$'))
print('\033[34m=-\033[m' * 20)
print('\033[1;36mFormas de pagamento:\033[m')
print('\033[1;34mDigite 1\033[m para pagamento em \033[1;32mcheque ou dinheiro!\033[m')
print('\033[1;34mDigite 2\033[m para pagamento no \033[1;32mcartão a vista!\033[m')
print('\033[1;34mDigite 3\033[m para pagamento no \033[1;32mcartão em 2x!\033[m')
print('\033[1;34mDigite 4\033[m para pagmento no \033[1;32mcartão em 3x ou mais!\033[m')
print('\033[34m=-\033[m' * 20)
paga = int(input('\033[1;34mQual forma de pagamento?\033[m '))
if paga == 1:
    prod = valor * 0.10
    print('Você terá um \033[34mdesconto\033[m de \033[32mR${:.2f}\033[m, e o valor ficará \033[32mR${:.2f}\033[m!!'.format(prod, valor - prod))
elif paga == 2:
    prod = valor * 0.05
    print('Você terá um \033[34mdesconto\033[m de \033[32mR${:.2f}\033[m, e o valor ficará \033[32mR${:.2f}\033[m!!'.format(prod, valor - prod))
elif paga == 3:
    print('Você não terá nenhum \033[34mdesconto\033[m ou \033[31mjuros\033[m, e o valor ficará \033[32mR${:.2f}\033[m!!'.format(valor))
elif paga == 4:
    prod = valor * 0.20
    print('Você terá um \033[31mjuros\033[m de \033[32mR${:.2f}\033[m, e o valor ficará \033[32mR${:.2f}\033[m!!'.format(prod, valor + prod))
else:
    print('\033[1;31mForma de pagamento inválida!\033[m')
print('Tenha um ótimo dia!')
