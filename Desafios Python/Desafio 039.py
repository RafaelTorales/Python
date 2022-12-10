from datetime import date
atual = date.today().year
ano = int(input('Qual ano você nasceu? '))
idade = atual - ano
print('''Qual seu gênero:
[ 1 ] Masculino
[ 2 ] Feminino''')
gen = int(input('Digite sua opção: '))
print('Você nasceu em {} e tem {} anos em {}.'.format(ano, idade, atual))
if idade < 18 and gen == 1:
    falt = 18 - idade
    print('Você \033[1;33mainda vai se alistar\033[m ao serviço militar e falta {} anos!'.format(falt))
    alis = atual + falt
    print('Seu alistamento vai ser em {}'.format(alis))
elif idade == 18 and gen == 1:
    print('Você \033[1;33mestá na hora de se alistar\033[m ao serviço militar!')
elif idade > 18 and gen == 1:
    falt = idade - 18
    print('Você já \033[1;33mpassou do tempo de se alistar\033[m ao serviço militar e já passou {} anos!'.format(falt))
    alis = atual - falt
    print('Seu alistamento foi em {}'.format(alis))
else:
    print('Você não precisa se alistar!')
print('Tenha um otimo dia!')
