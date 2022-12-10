listagem = ('Banana', 2.5,
            'Abacate', 4.5,
            'Abacaxi', 7,
            'Maça', 10,
            'Morango', 5.77)
print('-' * 37)
print(f'{"LISTAGEM DE PREÇOS":^37}')
print('-' * 37)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>.2f}')
print('-' * 37)