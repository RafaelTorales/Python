pessoas = list()
dados = list()
maipeso = menpeso = 0
while True: #Pede nome e peso para adicionar na lista 'Pessoas'
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maipeso = menpeso = dados[1]
    else:
        if dados[1] > maipeso:
            maipeso = dados[1]
        if dados[1] < menpeso:
            menpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    c = ' '
    while c not in 'NnSs':
        c = str(input('Quer continuar? [S/N] ')).strip()[0]
    if c in 'Nn':
        break
print('\033[34;1m-=\033[m' * 30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maipeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maipeso:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menpeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menpeso:
        print(f'[{p[0]}] ', end='')
