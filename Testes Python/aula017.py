num = [2, 5, 9, 1]
lista = [] #ou lista = list() #Começar lista vazia
num[0] = 0 #Troca o item da lista
num.append(0) #Adiciona o item no final da lista
num.insert(0, 0) #Adiciona o item onde quiser[(item), (local na lista)]
num.sort() #Deixa a lista em ordem crescente
num.sort(reverse=True) #Deixa a lista em ordem decrescente
elementos = len(num) #Conta quantos elementos tem na lista
num.pop() #Elimina o último valor
num.pop(0) #Elimina o valor indicado
if 0 in num: #Se tiver o '4' na lista irá remover
    num.remove(0) #Remove o valor indicado, o primeiro que achar na lista, se não tiver na lista da erro

valores = list()

for cont in range(0, 5): #Para ler valores e adicionar na lista
    valores.append(int(input('Digite um valor: ')))

for v in valores: #Para mostrar melhores os valores
    print(f'{v}...',end='')

for c, v in enumerate(valores): #Para mostrar os valores e sua respectiva posição
    print(f'Na posição {c} encontrei o valor {v}')

a = [2, 3, 4, 5]
b = a #Faz uma ligação entre elas
c = a[:] #Faz uma cópia dos valores

