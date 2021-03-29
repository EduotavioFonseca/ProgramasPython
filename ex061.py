# Jogando par ou ímpar com o computador
import random, time
computador = random.randint(1, 10)
teste = 'True'
cont = 0
while teste == 'True':
    numero = int(input('Digite um número de 1 a 10: '))
    print()
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper()
    soma = computador + numero
    if escolha == 'P' and soma % 2 == 0 or escolha == 'I' and soma % 2 != 0:
        time.sleep(1)
        print('Parabéns, você ganhou!!!')
        cont += 1
    else:
        time.sleep(1)
        print('Que pena, você perdeu.')
        teste = 'False'
    print()
    print(f'Você escolheu {numero} e o computador {computador}.')
    print('=' * 50)
print()
print(f'GAME OVER!!! Você ganhou {cont} vezes do computador.')
