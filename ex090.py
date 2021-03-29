# Função contador com passo.
import time
def contador(inicio, fim, passo):
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            time.sleep(1)
        print()
    else:
        if passo > 0:
            for c in range(inicio, fim - 1, - passo):
                print(c, end=' ')
                time.sleep(1)
            print()
        else:
            for c in range(inicio, fim - 1, passo):
                print(c, end=' ')
                time.sleep(1)
            print()


print('-x-' * 15)
contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
print('Agora é a sua vez!!!')
print()
i = int(input('Digite o número inicial: '))
print()
f = int(input('Digite o número final: '))
print()
p = int(input('Digite o passo: '))
print()
contador(i, f, p)
print('-x-' * 15)
