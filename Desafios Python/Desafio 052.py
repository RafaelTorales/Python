r = int(input('Digite um número: '))
a = 0
for c in range(1, r+1):
    if r % c == 0:
        print('\033[32m', end=' ')
        a += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(r, a))
if a == 2:
    print('É um número primo!')
else:
    print('Não é um número primo')
