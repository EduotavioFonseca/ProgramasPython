# Adivinhando número
import random, time
pensador = random.randint(0, 5)
numero = int(input('Digite um número de 0 a 5: '))
print()
print('Processando ...')
time.sleep(5)
if numero == pensador:
    print('Parabéns!!! Você escolheu {} e o computador também escolheu {}.'.format(numero, pensador))
else:
    print('TENTE DE NOVO. Você escolheu {} e o computador escolheu {}.'.format(numero, pensador))
