dist = float(input('Qual a distância percorrida em km? '))
print()
if dist > 200:
    print('O preço da passagem é: R$ {:.2f}.'.format(dist * 0.45))
else:
    print('O preço da passagem é: R$ {:.2f}.'.format(dist * 0.5))
