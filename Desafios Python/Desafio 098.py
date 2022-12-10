def contador(i, f, p):
    print('-=' * 30)
    if p < 0:
        p = abs(p)
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f:
        p *= -1
    if f <= i:
        f -= 1
    if f >= i:
        f += 1
    for c in range(i, f, p):
        print(f'{c} ', end='')
        sleep(0.3)
    print('FIM!')


# Programa Principal
from time import sleep

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')
contador(i=int(input('Início: ')),
         f=int(input('Final: ')),
         p=int(input('Passo: ')))
