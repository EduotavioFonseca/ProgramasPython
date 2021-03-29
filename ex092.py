# Lista e funções sorteia e soma par.
import random, time
lista = []
def sorteia():
    print('Os valores sorteados foram: ', end=' ')
    for i in range(0, 5):
        sorteio = random.randint(0, 100)
        print(f' {sorteio}', end=' ')
        time.sleep(1)
        lista.append(sorteio)

def somaPar():
    soma = 0
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    print(f'A soma dos valores é: {soma}')


sorteia()
print()
somaPar()
