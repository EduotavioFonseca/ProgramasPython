# Progressão aritmética
termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = int(input('Quantos termos deseja calcular? '))
an = 0
print()
print('Os {} primeiros termos da PA são: '.format(termos))
print()
for i in range(1, termos + 1):
    an = termo1 + (i - 1) * razao
    print(an, end=' ')
