lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
print('-=' * 20)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista! Nas posições ', end='')
    for r, t in enumerate(lista):
        if t == 5:
            print(f'{r}... ', end='')
else:
    print('O valor 5 não foi encontrado na lista!')
