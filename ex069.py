# Lista de Preços
lista = ('Lápis', '1.75', 'Borracha', '0.80', 'Caderno', '10.17', 'Estojo', '5.35', 'Mochila', '98.46', 'Caneta Azul',
         '2.76', 'Caneta Vermelha', '2.80', 'Apontador', '5.13')
print('=' * 50)
print()
print('{:^50}'.format('Lista de Compras '))
print()
print('=' * 50)
for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<40}', '{:>2}'.format("R$"), '{:>6}'.format(lista[i + 1]))
print('=' * 50)
