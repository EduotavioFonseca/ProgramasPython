# Tupla de 4 valores no teclado
num = (int(input('Digite um número de 1 a 10: ')), int(input('Digite um número de 1 a 10: ')),
       int(input('Digite um número de 1 a 10: ')), int(input('Digite um número de 1 a 10: ')))
print()
print(f'Você digitou os valores {num}')
print()
print(f'O número 9 apareceu {num.count(9)} vez(es).')
print()
if 3 in num:
    print(f'A posição do número 3 é: {num.index(3) + 1}')
else:
    print('O número 3 não foi digitado.')
print()
print(f'Os números pares são: ', end='')
for i in num:
    if i % 2 == 0:
        print(f'{i} ', end='')
