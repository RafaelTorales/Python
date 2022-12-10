r = 'S'
c = s = m = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um valor: '))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N]  ')).upper().strip()[0]
m = s / c
print('A média dos {} valores digitados é {:.2f}'.format(c, m))
print('O maior número é {} e o menor é {}'.format(maior, menor))
