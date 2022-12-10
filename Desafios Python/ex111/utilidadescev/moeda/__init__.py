def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco*2
    return res if formato is False else moeda(res)


def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(preco=0, moedaa='R$'):
    return f'{moedaa}{preco:>.2f}'.replace('.', ',')


def resumo(m=0, a=10, r=5):
    print('-' * 30)
    print('    RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(m)}')
    print(f'Dobro do preço: \t{dobro(m, True)}')
    print(f'Metade do preço: \t{metade(m, True)}')
    print(f'{a}% de aumento: \t{aumentar(m, a, True)}')
    print(f'{r}% de redução: \t{diminuir(m, r, True)}')
    print('-' * 30)
