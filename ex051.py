# Adivinhando número com while
import random, time
pensador = random.randint(0, 10)
numero = int(input('Digite um número de 0 a 10: '))
cont = 1
while numero != pensador:
    cont += 1
    print()
    print('Processando ...')
    time.sleep(1)
    print()
    numero = int(input('Numero errado. Digite outro número de 0 a 10: '))
print()
print('Parabéns!!! Você acertou o numero {} em {} tentativas.'.format(numero, cont))
