# Matriz 3 x 3
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = (int(input(f'Digite o elemento [{i}][{j}]: ')))
print()
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]:^4}]', end='')
    print()
