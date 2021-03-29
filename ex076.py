# Lê nome e peso de várias pessoas
lista1 = []
lista2 = []
while True:
    lista1.append(str(input('Digite o nome: ')))
    lista1.append(float(input('Qual o peso? ')))
    lista2.append(lista1[:])
    lista1.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    print()
    if resp == 'N':
        break
print()
print(f'Foram cadastradas {len(lista2)} pessoas.')
print()
print('As pessoas mais pesadas são: ', end='')
for c, v in lista2:
    if v >= 100:
        print(f' {c} ', end='')
print()
print()
print('As pessoas mais leves são: ', end='')
for c, v in lista2:
    if v <= 70:
        print(f' {c} ', end='')
print()
