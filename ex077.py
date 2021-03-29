# Separar pares e ímpares
lista = []
listapar = []
listapar1 = []
listaimpar = []
for i in range(0, 7):
    num = (int(input('Digite um número inteiro: ')))
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
print()
lista.append(listapar)
lista.append(listaimpar)
lista[0].sort()
lista[1].sort()
print(f'A lista de pares e ímpares é: {lista}')
print()
print(lista)
