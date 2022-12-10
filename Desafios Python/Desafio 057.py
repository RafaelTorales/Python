'''s = 'a'
while s not in 'MmFf':
    s = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
    if s not in 'MmFf':
        print('Favor digitar M ou F!')
if s == 'M':
    s = 'Masculino'
else:
    s = 'Feminino'
print('Seu sexo é {}'.format(s))'''
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, infome seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
