# Lê nome e preço de produtos usando while e break
soma = contp = menor = 0
aux = 1
barato = ' '
while True:
    print(f'------   {aux}° Produto   ------')
    produto = str(input('Digite o nome do produto: ')).lower()
    preco = float(input('Digite o preço do produto R$ '))
    print('---------------------------')
    print()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    print()
    soma += preco
    if preco > 1000:
        contp += 1
    if aux == 1 or preco < menor:
        menor = preco
        barato = produto
    aux += 1
    if resp == 'N':
        break
print('= # =' * 10)
print()
print(f'O total gasto na compra foi R$ {soma:.2f}.')
print()
print(f'{contp} produtos custam mais de R$ 1.000,00.')
print()
print(f'O produto mais barato é {barato} e ele custa R$ {menor:.2f}.')
print()
print('= # =' * 10)
