# Maioridade 21 anos
from datetime import date
cont1 = cont2 = 0
for i in range(0, 7):
    aux = int(input('Digite o ano de de nascimento: '))
    idade = date.today().year - aux
    if idade < 21:
        cont1 += 1
    else:
        cont2 += 1
print()
print('Temos {} pessoas menores de idade e {} pessoas maiores de idade.'.format(cont1, cont2))
