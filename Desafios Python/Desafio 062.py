print('=' * 20)
print('\033[1;34m TERMOS DE UMA PA\033[m')
print('=' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
l = 0
t = 1
while t != 0:
    l += 1
    print(p, end=' → ')
    p += r
    c += 1
    if c == 10:
        print('PAUSA')
        t = int(input('\nQuantos termos a mais você quer? '))
        c = c - t
print('Progressão finalizada com {} termos mostrados.'.format(l))
