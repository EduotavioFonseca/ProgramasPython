# Soma de vários números, média, maior e menor. Uso de fstring.
numero = i = soma = media = menor = maior = 0
cont = 0
teste = 'S'
while teste == 'S':
    numero = int(input('Digite um número inteiro: '))
    cont += 1
    soma += numero
    if cont == 1:
        menor = numero
        maior = numero
    else:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
    print()
    teste = str(input('Quer continuar? [S/N] ')).upper()
    print()
media = soma/cont
print()
print('=x=' * 15)
print('Você digitou {} números e a média deles é {}'.format(cont, media))
print()
print(f'O menor número é {menor} e o maior é {maior}')
print('=x=' * 15)
