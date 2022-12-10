dados = dict()
gols = list()
jogadores = list()
total = 0
while True:
    print('-' * 30)
    dados['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    dados['gols'] = gols[:]
    for i in gols:
        total += i
    gols.clear()
    dados['total'] = total
    jogadores.append(dados.copy())
    total = 0
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    a = int(input('Mostrar dados de qual jogador? '))
    if a == 999:
        break
    if a >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {a}! Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[a]["nome"]}:')
        for i, v in enumerate(jogadores[a]['gols']):
            print(f'  No jogo {i} fez {v} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
