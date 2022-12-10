'''km = float(input('Qual vai ser a distancia da sua viagem? '))
if km <= 200:
    print('O preço da passagem é R$ {:.2f}! '.format(km * 0.5))
else:
    print('O preço da passagem é R$ {:.2f}! '.format(km * 0.45))'''

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
