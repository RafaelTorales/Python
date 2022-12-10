dados = dict()
tdados = list()
media = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    while dados['Sexo'] not in 'MmFf':
        dados['Sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    dados['Idade'] = int(input('Idade: '))
    tdados.append(dados.copy())
    dados.clear()
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'NnSs':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'- O grupo tem {len(tdados)} pessoas.')
for c in range(0, len(tdados)):
    media += tdados[c]['Idade'] / len(tdados)
print(f'- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for c in range(0, len(tdados)):
    if tdados[c]['Sexo'] in 'F':
        print(tdados[c]['Nome'], end=' ')
print('\n- Lista das pessoas que estão acima da média:')
print()
for c in range(0, len(tdados)):
    if tdados[c]['Idade'] > media:
        print(tdados[c])
        print()
print('<< ENCERRADO >>')
