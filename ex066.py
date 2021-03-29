# Tabela do Brasileirão
times = ('Internacional', 'São Paulo', 'Flamengo', 'Atlético-MG', 'Palmeiras', 'Grêmio', 'Fluminense', 'Ceará',
         'Santos', 'Corinthians', 'Bragantino', 'Athletico', 'Atlético-GO', 'Sport', 'Vasco', 'Fortaleza', 'Bahia',
         'Goiás', 'Coritiba', 'Botafogo')
while True:

    print()
    print(f'Os 5 primeiros colocados são: {times[0:5]}')
    print()
    print(f'Os 4 últimos colocados são: {times[16:]}')
    print()
    print(f'Times: {sorted(times)}')
    print()
    print(f'O Bragantino está na posição: {times.index("Bragantino")+1}')
    break
