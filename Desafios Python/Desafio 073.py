times = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG',
         'Chapecoense', 'América-MG', 'Bragantino', 'Goiás', 'São Paulo', 'Fortaleza', 'Botafogo', 'Ceará', 'Cuiabá',
         'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
