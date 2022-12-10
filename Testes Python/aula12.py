nome = str(input('Qual é seu nome? '))
if nome == 'Rafael':
    print('Que nome bonito')
elif nome == 'João' or nome == 'Cleber':
    print('Nome de pedreiro ein')
elif nome in 'Miriã Gabriela':
    print('Que nome lindo!')
else:
    print('Que nome normalzinho ein.')
print('Tenha um bom dia, {}!'.format(nome))
