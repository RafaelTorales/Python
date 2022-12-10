print('Vamos calcular seu IMC!!!')
peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é sua altura? '))
imc = peso / (altura * altura)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Está \033[1;34mABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Está no \033[1;34mPESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Está em \033[1;34mSOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Está em \033[1;34mOBESIDADE!')
else:
    print('Está em \033[1;34mOBESIDADE MÓRBIDA!'.format(imc))
