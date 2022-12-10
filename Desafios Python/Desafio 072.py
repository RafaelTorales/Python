num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
       'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezeoito', 'Dezenove', 'Vinte')
#r = int(input('Digite um número entre 0 a 20: '))
#while r < 0 or r > 20:
#    r = int(input('Tente novamente. Digite um número entre 0 a 20: '))
while True:
       r = int(input('Digite um número entre 0 e 20: '))
       if 0 <= r <= 20:
              print(f'Você digitou o número \033[1;34m{num[r]}\033[m')
              c = str(input('Você quer continuar? [N/S] ')).strip().upper()[0]
              if c in 'N':
                     break
       print('Tente novamente. ', end='')
print('Programa finalizado')
