def area(larg, comp):
    tam = larg * comp
    print(f'A área de um terro {larg}x{comp} é de {tam}m².')


# Programa Principal
print('Controle de Terrenos')
print('-' * 20)
area(larg=float(input('LARGURA (m): ')),
     comp=float(input('COMPRIMENTO (m): ')))
