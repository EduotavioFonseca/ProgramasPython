num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = int(input('Digite um terceiro número inteiro: '))
if num1 > num2:
    aux1 = num1
    aux2 = num2
else:
    aux1 = num2
    aux2 = num1
print()
if num3 > aux1:
    print('O número {} é o maior e o número {} é o menor.'.format(num3, aux2))
else:
    if num3 > aux2:
        print('O número {} é o maior e o número {} é o menor.'.format(aux1, aux2))
    else:
        print('O número {} é o maior e o número {} é o menor.'.format(aux1, num3))
