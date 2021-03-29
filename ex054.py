# Progressão aritmética com while
termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = int(input('Quantos termos deseja calcular? '))
an = termo1
print()
print('Os {} primeiros termos da PA são: '.format(termos), end='')
i = 1
while i < termos + 1:
    print(an, end=' ')
    an += razao
    i += 1
