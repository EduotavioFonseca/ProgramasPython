# Número primo
n1 = int(input('Digite um número inteiro: '))
print()
cont = 0
for i in range(1, n1 + 1):
    if n1 % i == 0:
        cont += 1
if cont == 2:
    print('O número {} é primo.'.format(n1))
else:
    print('O número {} não é primo.'.format(n1))
