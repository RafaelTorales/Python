a = h = m = 0
while True:
    print('-' * 23)
    print('CADASTRE UMA PESSOA')
    print('-' * 23)
    i = int(input('Idade: '))
    if i >= 18:
        a += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        h += 1
    elif sexo == 'F' and i < 20:
        m += 1
    print('-' * 23)
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'''Total de pessoas com mais de 18 anos:{a}
Ao todo temos {h} homens cadastrados
E temos {m} mulheres com menos de 20 anos''')
