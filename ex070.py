# Contagem de vogais
vogais = ('a', 'e', 'i', 'o', 'u')
frase = ('rapidamente', 'alvoreceu', 'aurora', 'controle', 'carapucuiba', 'fantoche', 'lobinho', 'certo',
           'adamantium')
for palavra in frase:
    print(f'A palavra {palavra.upper()} contém: ', end=' ')
    for j in range(0, len(palavra)):
        for k in range(0, 5):
            if palavra[j] == vogais[k]:
                print(f'{palavra[j]}', end=' ')
    print()
