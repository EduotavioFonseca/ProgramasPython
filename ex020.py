# Procurando letra na palavra
frase = str(input('Escreva uma frase: ')).strip().lower()
print()
print('A letra "a" aparece {} vezes.'.format(frase.count('a')))
print()
aux1 = frase.split()
print('O primeiro "a" aparece na posição {}.'.format(frase.find('a')+1))
print()
print('O último "a" aparece na posição {}.'.format(frase.rfind('a')+1))
