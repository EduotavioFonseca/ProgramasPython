# Soma dos pares
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = int(input('Digite o terceiro número inteiro: '))
n4 = int(input('Digite o quarto número inteiro: '))
n5 = int(input('Digite o quinto número inteiro: '))
n6 = int(input('Digite o sexto número inteiro: '))
num = [n1, n2, n3, n4, n5, n6]
soma = 0
for i in range(0, 6):
    if num[i] % 2 == 0:
        soma += num[i]
print()
print('A soma dos números pares é {}.'.format(soma))
