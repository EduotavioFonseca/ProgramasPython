# Matriz 3 x 3 e cálculos
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = somapar = 0
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = (int(input(f'Digite o elemento [{i}][{j}]: ')))
print()
print('=' * 40)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]:^4}]', end='')
        if lista[i][j] % 2 == 0:
            somapar += lista[i][j]
    print()
print()
print(f'A soma de todos os valores pares é: {somapar}')
print()
for i in range(0, 3):
    soma += lista[i][2]
print(f'A soma dos valores da 3ª coluna é: {soma}')
print()
for i in range(0, 3):
    if i == 0 or lista[1][i] > maior:
        maior = lista[1][i]
print(f'O maior valor da 2ª linha é: {maior}')
