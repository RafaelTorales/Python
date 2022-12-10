matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
'''matriz = list()
numeros = list()
cont = 0
while True:
    for n in range(0, 3):
        numeros.append(int(input(f'Digite um valor para [{cont}, {n}]: ')))
    matriz.append(numeros[:])
    numeros.clear()
    cont += 1
    if cont == 3:
        break
print('-=' * 30)
for h in range(0, 3):
    for n in matriz[h]:
        print(f'[{n:^5}]', end='')
    print()'''
