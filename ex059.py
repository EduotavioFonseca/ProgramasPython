# Soma de vários números. Usa comando break
cont = soma = 0
while True:
    numero = int(input('Digite um número inteiro [999 para parar]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
    print()
print()
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))
