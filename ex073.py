# Colocar números na ordem crescente sem o sort
lista = []
lista1 = []
for i in range(0, 5):
    lista.append(int(input('Digite um número inteiro: ')))
    print()
print(f'A lista original é: {lista}')
for k in range(0,5):
    lista1.append(min(lista))
    lista.remove(min(lista))
print()
print(f'A lista ordenada é: {lista1}')
