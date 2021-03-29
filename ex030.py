print()
numero = int(input('Digite um número inteiro: '))
print()
print('Escolha uma das opções abaixo:')
print()
print('x=' * 20)
print('1 - Conversão para binário.')
print('2 - Conversão para octal.')
print('3 - Conversão para hexadecimal.')
print('x=' * 20)
print()
opcao = int(input('Digite a opção: '))
if opcao == 1:
    resp = bin(numero)[2:]    # Elimina os 2 primeiros caracteres
    tipo = str('binário')
elif opcao == 2:
    resp = oct(numero)[2:]
    tipo = str('octal')
elif opcao == 3:
    resp = hex(numero)[2:]
    tipo = str('hexadecimal')
else:
    print('Opção inválida. Digite a opção correta!!!')
print()
print('x=' * 40)
print()
print("O número {} convertido para {} é igual a: {}".format(numero, tipo, resp))
print()
print('x=' * 40)
