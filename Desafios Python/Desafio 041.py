from datetime import date
ano = int(input('Qual ano você nasceu? '))
idade = date.today().year - ano
print('O atleta tem {} anos!'.format(idade))
if idade <= 9:
    print('Categoria: \033[1;32mMIRIM')
elif idade <= 14:
    print('Categoria: \033[1;36mINFANTIL')
elif idade <= 19:
    print('Categoria: \033[1;35mJUNIOR')
elif idade <= 25:
    print('Categoria: \033[1;34mSÊNIOR')
else:
    print('Categoria: \033[1;31mMASTER')
