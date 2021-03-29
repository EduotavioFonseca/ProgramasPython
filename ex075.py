# Lista com vários números, lista de pares e lista de ímpares
lista = []
listapar = []
listaimpar = []
while True:
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        lista.append(num)
        listapar.append(num)
    else:
        lista.append(num)
        listaimpar.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    print()
    if resp == 'N':
        break
print()
print(f'A lista original é: {lista}')
print()
print(f'A lista de pares é: {listapar}')
print()
print(f'A lista de ímpares é: {listaimpar}')
