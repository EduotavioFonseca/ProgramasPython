# Soma de vários números
numero = i = soma = 0
cont = -1
while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Digite um número inteiro [999 para]: '))
    print()
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))
