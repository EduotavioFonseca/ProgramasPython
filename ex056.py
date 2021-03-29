# PA com while aninhado
termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
#termos = int(input('Quantos termos deseja calcular? '))
an = termo1
mais = 10
print()
print('Os {} primeiros termos da PA são: '.format(mais), end='')
i = 1

total = 0
while mais != 0:
    total += mais
    while i < total + 1:
        print(an, end=' ')
        an += razao
        i += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer a mais? '))
print('FIM')
