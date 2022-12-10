num = int(input('Digite um número para ver a tabuada: '))
print('=' * 20)
for c in range(1, 11,):
    print('{} x {:2} = {}'.format(num, c, c * num))
print('=' * 20)
