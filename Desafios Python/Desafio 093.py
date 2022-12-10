dados = dict()
gols = list()
total = 0
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c, i in enumerate(gols):
    print(f'=> Na partida {c+1}, fez {i} gols.')
print(f'Foi um total de {total} gols.')
print(f'A média de gols por partida foi de {total/partidas:.1f}')
