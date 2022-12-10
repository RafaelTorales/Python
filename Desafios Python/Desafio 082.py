a = list()
b = list()
d = list()
while True:
    a.append(int(input('Digite um número: ')))
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
for r, t in enumerate(a):
    if t % 2 == 0:
        b.append(t)
    else:
        d.append(t)
print('-=' * 20)
print(f'A lista completa é {a}')
print(f'A lista de pares é {b}')
print(f'A lista de ímpares é {d}')
