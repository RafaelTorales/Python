media = 0
velho = 0
mulher = 0
nomevelho = ''
for c in range(1, 5):
    print('\033[1;34m---- {}ª PESSSOA ----\033[m'.format(c))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media += idade / 4
    if sexo == 'F':
        if idade < 20:
            mulher += 1
    if c == 1 and sexo == 'M':  #ou sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if idade > velho and sexo == 'M':
            velho = idade
            nomevelho = nome
print('A média de idade do grupo é de {:.2f} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
