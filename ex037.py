preco = float(input('Digite o preço do produto que você quer comprar: R$ '))
print()
print('{:=^45}'.format(' LOJAS EDUARDO '))
print()
print('{:=^45}'.format('Escolha uma das opções abaixo'))
print()
print('1 - À vista dinheiro/cheque')
print('2 - À vista no cartão')
print('3 - Em até 2x no cartão')
print('4 - 3x ou mais no cartão')
print()
print('=x=' * 15)
opc = int(input('Qual a sua opção? '))
print()
if opc == 1:
    print('O preço final do produto é R$ {:.2f}.'.format(0.9 * preco))
elif opc == 2:
    print('O preço final do produto é R$ {:.2f}.'.format(0.95 * preco))
elif opc == 3:
    print('O preço final do produto é R$ {:.2f}.'.format(preco))
    print('Você vai pagar 2x de R$ {:.2f}.'.format(preco/2))
elif opc == 4:
    parcela = int(input('Quantas parcelas? '))
    print()
    print('O preço final do produto é R$ {:.2f}.'.format(1.2 * preco))
    print('Você vai pagar {}x de R$ {:.2f}.'.format(parcela, 1.2 * preco/parcela))
else:
    print('Opção inválida. Tente outra vez')
print('=x=' * 15)
