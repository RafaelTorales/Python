print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
t = int(input('Quantos termos você quer mostrar? '))
c = 1
a = 0
p = 1
s = 1
while c <= t:
    print(a,end=' - ')
    s = p + a
    a = p
    p = s
    c += 1
print('Fim')
