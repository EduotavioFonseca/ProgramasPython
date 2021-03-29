# Lista dentro de dicionário
campeonato = dict()
gol = []
aux = 0
campeonato['Jogador'] = str(input('Digite o nome do jogador: '))
print()
partidas = int(input('Quantas partidas ele jogou? '))
print()
for i in range(0, partidas):
    aux = int(input(f'Quantos gols na partida {i + 1}? '))
    gol.append(aux)
print()
campeonato['Gols'] = gol[:]
campeonato['Total'] = sum(gol)
print('=' * 55)
print()
print(campeonato)
print()
print('=' * 55)
print()
for k, v in campeonato.items():
    print(f'O campo {k} tem o valor: {v}')
print()
print('=' * 55)
print(f'O jogador {campeonato["Jogador"]} jogou {partidas} partidas.')
print()
for i in range(0, partidas):
    print(f'Na partida {i + 1} ele fez {gol[i]} gol(s).')
print()
print(f'No total ele fez {campeonato["Total"]} gols.')
print('=' * 55)
