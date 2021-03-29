# Maior e menor com lista
lista = []
for i in range(0, 5):
    lista.append(int(input('Digite um número inteiro: ')))
print()
print(f'O menor número é {min(lista)} e sua posição é:', end=' ')
for j in range(0, 5):
    if lista[j] == min(lista):
        pos = lista.index(lista[j], j) + 1
        print(f' {pos} ', end=' ')
print()
print()
print(f'O maior número é {max(lista)} e sua posição é:', end=' ')
for k in range(0, 5):
    if lista[k] == max(lista):
        pos = lista.index(lista[k], k) + 1
        print(f' {pos} ', end=' ')
