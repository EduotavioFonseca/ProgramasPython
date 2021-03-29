# Caixa eletrônico com while e break
while True:
    print(f'---------   CAIXA ELETRÔNICO BANCO EDUARDO S/A  ---------')
    valor = int(input('Digite o valor a ser sacado R$ '))
    print()
    print('Temos notas de R$ 50, R$ 20, R$ 10 e R$1 ')
    print('-' * 80)
    print()
    not50 = valor // 50
    resto50 = valor % 50
    not20 = resto50 // 20
    resto20 = resto50 % 20
    not10 = resto20 // 10
    not1 = resto20 % 10
    print(f'O valor R$ {valor} será fornecido em:')
    print(f'{not50} cédula(s) de R$ 50 - ' if not50 != 0 else '', f'{not20} cédula(s) de R$ 20 - ' if not20 != 0 else '',
          f'{not10} cédula(s) de R$ 10 - ' if not10 != 0 else '', f'{not1} cédula(s) de R$ 1' if not1 != 0 else '')
    print()
    if valor == 0:
        break
