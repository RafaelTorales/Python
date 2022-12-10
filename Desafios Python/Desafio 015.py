a = float(input('Quantos dias alugados? '))
b = float(input('Quantos Km rodados? '))
p = (a * 60) + (b * 0.15)
print('O total a pagar é de R${:.2f}'.format(p))
