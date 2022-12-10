esc = 0
result = 0
n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))
while esc != 5:
      print('\033[34mEscolha a opção!\033[m\n'
            '\033[36m[1]\033[m Somar\n'
            '\033[36m[2]\033[m Multiplicar\n'
            '\033[36m[3]\033[m Maior\n'
            '\033[36m[4]\033[m Novos números\n'
            '\033[36m[5]\033[m Sair do programa')
      esc = int(input('Digite a opção: '))
      if esc == 1:
            result = n1 + n2
            print('A soma dos números solicitados é {:.1f}\n'.format(result))
      if esc == 2:
            result = n1 * n2
            print('A multiplicação dos números solicitados é {:.1f}\n'.format(result))
      if esc == 3:
            if n1 > n2:
                  result = n1
                  print('O maior número é {}\n'.format(result))
            if n2 > n1:
                  result = n2
                  print('O maior número é {}\n'.format(result))
            if n1 == n2:
                  print('Não tem número maior!\n')
      if esc == 4:
            n1 = float(input('Digite o 1º valor: '))
            n2 = float(input('Digite o 2º valor: '))
      if esc == 5:
            print('Você saiu do programa!')
      else:
            print('Opção inválida! Tente novamente')
print('Muito obrigado!')
