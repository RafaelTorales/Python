print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
t = m = b = w = 0
a = 'A'
while True:
    p = str(input('Nome do Produto: ')).strip().capitalize()
    v = int(input('Preço: R$'))
    t += v
    w += 1
    if v > 1000:
        m += 1
    if w == 1 or v < b:
        b = v
        a = p
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print(f'''O total da compra foi R${t:.2f}
Temos {m} produtos custando mais de R$1000.00
O produto mais barato foi {a} que custa R${b:.2f}''')
