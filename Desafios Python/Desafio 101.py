def voto(ano=0):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
