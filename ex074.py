# Lista com vários números, números digitados, quantidade, ordem decrescente, 5 presente na lista
lista = []
while True:
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    print()
    if resp == 'N':
        break
print(f'A lista original é: {lista}')
print()
print(f'Foram digitados {len(lista)} números.')
print()
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
print()
n = lista.count(5)
if n == 0:
    print('O número 5 não foi digitado.')
if n == 1:
    print('O número 5 foi digitado 1 vez.')
else:
    print(f'O número 5 foi digitado {n} vezes.')
