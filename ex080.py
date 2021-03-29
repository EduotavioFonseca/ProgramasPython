# Jogo da megasena
import random, time
aposta = []
num = int(input('Quantas apostas deseja fazer? '))
print()
for i in range(0, num):
    for j in range(0, 6):
        n1 = random.randint(1, 60)
        while n1 in aposta:
            n1 = random.randint(1, 60)
        aposta.append(n1)
    aposta.sort()
    print(f'Jogo {i+1}: {aposta}')
    time.sleep(2)
    aposta.clear()
