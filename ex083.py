# 4 jogadores jogam um dado. Guarda em um dicionário e coloca em ordem.
import random
import time
from operator import itemgetter
lista = []
resultado = {'Jogador 1': random.randint(1, 6), 'Jogador 2': random.randint(1, 6), 'Jogador 3': random.randint(1, 6),
             'Jogador 4': random.randint(1, 6)}
print()
print('     Valores Sorteados')
print()
for k, v in resultado.items():
    print(f'   O {k} tirou: {v}')
    time.sleep(2)
print()
print('=' * 35)
print()
lista = sorted(resultado.items(), key=itemgetter(1), reverse=True)
print('      Ranking dos Jogadores')
print()
for i, v in enumerate(lista):
    print(f'   {i+1}° lugar:  {v[0]} com {v[1]}')
    time.sleep(2)
print()
print('=' * 35)
