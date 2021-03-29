# Função área
def area(l, c):
    a = l * c
    print('                      Controle de Terreno ')
    print('-' * 60)
    print(f'Largura (m): {l:.2f}')
    print(f'Comprimento (m): {c:.2f}')
    print(f'A área de um terreno de {l:.2f} x {c:.2f} é de: {a:.2f} m².')
    print('-' * 60)


larg = float(input('Digite a largura do terreno em m: '))
print()
comp = float(input('Digite o comprimento do terreno em m: '))
print()
area(larg, comp)
