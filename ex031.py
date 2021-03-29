num1 = int(input('Digite um número inteiro: '))
print()
num2 = int(input('Digite outro número inteiro: '))
print()
if num1 > num2:
    print('O número {} é maior que {}.'.format(num1, num2))
elif num1 < num2:
    print('O número {} é menor que {}.'.format(num1, num2))
else:
    print('Os números são iguais.')
