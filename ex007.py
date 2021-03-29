# Dinheiro na carteira
n1 = float(input('Quanto dinheiro você tem na carteira? '))
n2 = float(input('Qual a cotação do dólar? '))
print()
print('Considerando US$ 1 = R$ {}, você tem US$ {:.2f} na carteira.'.format(n2, n1/n2))
