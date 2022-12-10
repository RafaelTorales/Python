while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if t < 0:
        break
    for c in range(1, 11):
        print(f'{t} x {c} = {t*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
