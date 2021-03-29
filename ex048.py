# Maior e menor peso
menor = maior = 0
for i in range(1, 6):
    peso = float(input('Digite o seu peso em kg: '))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print()
print('O menor peso é {} kg e o maior peso vale {} kg.'.format(menor, maior))
