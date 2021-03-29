# Aprimoramento do ex. 085
campeonato = dict()
gol = []
tabela = []
aux = 0
while True:
    campeonato.clear()
    campeonato['Jogador'] = str(input('Digite o nome do jogador: '))
    print()
    partidas = int(input('Quantas partidas ele jogou? '))
    print()
    for i in range(0, partidas):
        aux = int(input(f'    Quantos gols na partida {i + 1}? '))
        gol.append(aux)
    print()
    campeonato['Gols'] = gol[:]
    campeonato['Total'] = sum(gol)
    tabela.append(campeonato.copy())
    gol.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO!!! Digite apenas S ou N.')
    print()
    print()
    if resp == 'N':
        break
print('=' * 55)
print()
print(tabela)
print()
print('=' * 55)
print()
print('  Código   Nome               Gols        Total ')
for k, v in enumerate(tabela):
    print(f'{k:^10}', end=' ')
    for d in v.values():
        print(f'{str(d):<16}', end=' ')
    print()
print()
print('=' * 55)
while True:
    aux1 = int(input('Mostrar dados de qual jogador? [999 para sair] '))
    print()
    if aux1 == 999:
        break
    if aux1 >= len(tabela):
        print(f'Erro!!! Digite outro número.')
    else:
        print(f'Levantamento de {tabela[aux1]["Jogador"]}')
        print()
        for i, g in enumerate(tabela[aux1]["Gols"]):
            print(f'   No jogo {i + 1} ele fez {g} gols.')
            print()
print('=' * 55)
