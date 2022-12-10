from random import randint
from time import sleep
m = 'JOGA NA MESA SENA'
sena = list()
print('-' * 30)
print(f'{m:^30}')
print('-' * 30)
q = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {q} JOGOS -=-=-=')
for j in range(1, q+1):
    for a in range(0, 6):
        n = randint(0, 60)
        if n not in sena:
            sena.append(n)
        else:
            while n in sena:
                n = randint(0, 60)
            if n not in sena:
                sena.append(n)
    sena.sort()
    print(f'Jogo {j}: {sena}')
    sleep(1)
    sena.clear()
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
