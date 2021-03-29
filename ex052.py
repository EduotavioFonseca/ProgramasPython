# Menu com várias operações
print('#'*40)
print()
print('{:^40}'.format('MENU DE OPÇÕES'))
print()
print('            {}'.format('[1] SOMAR'))
print('            {}'.format('[2] MULTIPLICAR'))
print('            {}'.format('[3] MAIOR'))
print('            {}'.format('[4] NOVOS NÚMEROS'))
print('            {}'.format('[5] SAIR'))
print()
print('#'*40)
print()
opc = 0
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print()
while opc != 5:
    opc = int(input('Escolha uma opção: '))
    print()
    if opc == 1:
        soma = n1 + n2
        print('A soma é igual a {}'.format(soma))
    elif opc == 2:
        mult = n1 * n2
        print('A multiplicação é igual a {}'.format(mult))
    elif opc == 3:
        if n1 > n2:
            print('O maior número entre os dois é {}'.format(n1))
        elif n1 < n2:
            print('O maior número entre os dois é {}'.format(n2))
        else:
            print('Os números {} e {} são iguais'.format(n1, n2))
    elif opc == 4:
        print('Digite dois outros números: ')
        print()
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif opc == 5:
        print('FIM DO PROGRAMA.')
    else:
        print()
        print('Opção inválida. Veja o MENU !!!')
    print()
