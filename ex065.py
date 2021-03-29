# Tupla com números por extenso
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
k = int(input('Digite um número de 0 a 20: '))
while k not in range(0, 21):
    print('Número Inválido!!!')
    k = int(input('Digite um número de 0 a 20: '))
print()
print(f'O número digitado foi {num[k]}.')
