# Tabuada com loop for
print('*' * 50)
print()
print('{:^50}'.format('Jogo da Tabuada'))
print()
print('*' * 50)
print()
op = input('Escolha a tabuada que você quer ( + * / ): ')
num = int(input('Escolha um número de 1 a 10: '))
print()
print('*' * 50)
if op == '+':
    print('{:^50}'.format('A tabuada de {} do número {} é:'.format('somar', num)))
    for i in range(1,11):
            print('{} {} {} = {}'.format(num, op, i, num + i))
elif op == '*':
    print('{:^50}'.format('A tabuada de {} do número {} é:'.format('multiplicar', num)))
    for i in range(1, 11):
            print('{} {} {} = {}'.format(num, op, i, num * i))
else:
    print('{:^50}'.format('A tabuada de {} do número {} é:'.format('dividir', num)))
    for i in range(1, 11):
            print('{} {} {} = {}'.format(num * i, op, num, int((num * i) / num)))
print('*' * 50)
