# Função que lê vários parâmetros e diz qual o maior.
import time
def maior(*num):
    print('Analisando os valores... ')
    for i in range(0, len(num)):
        print(num[i], end=' ')
        time.sleep(1)
    print(f'   Foram informados {len(num)} valores.')
    print(f'O maior valor foi {max(num)}.')
    print('=^=' * 20)


maior(2, 5, 6, 4, 8)
maior(2, 5, 6, 4, 1, 7, 20)
maior(-32, -25, -6, -40, -100, -7, -20)
