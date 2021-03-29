# Soma de ímpares múltiplos de 3 de 1 a 500
soma = 0
numeros = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        numeros += 1
        soma += i
print(' A soma dos {} números ímpares divisíveis por 3 é: {}'.format(numeros, soma))
