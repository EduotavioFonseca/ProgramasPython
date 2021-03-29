# Fatorial
numero = int(input('Digite um número inteiro: '))
fat = 1
cont = numero
print('{}! = '.format(numero), end='')
if numero < 0:
    print('Não existe fatorial de número negativo.')
else:
    while cont > 0:
        print('{}'.format(cont), end='')
        print(' x ' if cont > 1 else ' = ', end='')
        fat *= cont
        cont -= 1
    print('{}.'.format(fat))
