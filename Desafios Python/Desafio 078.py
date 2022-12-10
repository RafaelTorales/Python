valores = list()
for cont in range(0, 5): #Pede para o usuário 5 números inteiros
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
maior = menor = valores[0] #Faz o primeiro valor ser o maior e e menor
for c, v in enumerate(valores): #Verifica o maior e o menor
    if valores[c] > maior:
        maior = valores[c]
    if valores[c] < menor:
        menor = valores[c]
print('=-' * 20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for r, t in enumerate(valores):
    if t == maior:
        print(f'{r}... ', end='') #Verifica em qual posição está o maior número
print(f'\nO menor valor digitado foi o {menor} nas posições ', end='')
for r, t in enumerate(valores):
    if t == menor:
        print(f'{r}... ', end='') #Verifica em qual posição está o menor número
