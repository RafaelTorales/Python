n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
nota = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(n1, n2, nota))
if nota < 5:
    print('O aluno está \033[1;31mREPROVADO!\033[m')
elif nota >= 7:
    print('O aluno está \033[1;32mAPROVADO!\033[m')
else:
    print('O aluno está \033[1;33mRECUPERAÇÃO!\033[m')
