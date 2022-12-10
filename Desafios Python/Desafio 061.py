print('=' * 20)
print('\033[1;34m10 TERMOS DE UMA PA\033[m')
print('=' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c != 10:
    print(p, end=' → ')
    p += r
    c += 1
print('ACABOU')
