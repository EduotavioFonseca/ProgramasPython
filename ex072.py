# Lista com vários números. Adicionar números diferentes.
lista = []
while True:
    num = int(input('Digite um número inteiro: '))
    if num not in lista:
        lista.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    print()
    if resp == 'N':
        break
lista.sort()
print(f'A lista é: {lista}')
