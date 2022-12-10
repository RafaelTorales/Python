casa = float(input('Qual o valor da casa que você quer comprar? R$'))
sal = float(input('Qual seu salário? R$'))
ano = float(input('Em quantos anos você quer pagar a casa? '))
mes = (ano * 12)
valor = casa / mes
if valor > sal * 0.30:
    print ('Infelizmente você não pode financiar essa casa.')
else:
    print('Você terá que pagar \033[4;32mR${:.2f}\033[m por {:.0f} meses, para quitar em {:.0f} ano(s)!'.format(valor, mes, ano))
