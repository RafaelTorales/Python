sal = float(input('Qual é o salário do funcionario? R$'))
if sal > 1250.00:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, sal + (sal/10)))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, sal + (sal * 0.15)))
