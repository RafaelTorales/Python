print('=' * 20)
print('\033[1;34m10 TERMOS DE UMA PA\033[m')
print('=' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
a = p + (10 - 1) * r
for c in range(p, a + r, r):
    print(c,end=' → ')
print('ACABOU')
