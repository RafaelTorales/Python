lista = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        print('Valor adicionado com sucesso...')
        lista.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
lista.sort()
print('=-' * 20)
print(f'Você digitou os valores {lista}')
