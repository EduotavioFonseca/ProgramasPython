# Ordem de apresentação
from random import shuffle
al1 = input('Qual o nome do primeiro aluno? ')
print()
al2 = input('Qual o nome do segundo aluno? ')
print()
al3 = input('Qual o nome do terceiro aluno? ')
print()
al4 = input('Qual o nome do quarto aluno? ')
lst = [al1, al2, al3, al4]
shuffle(lst)
print()
print('A ordem de apresentação será: {} .'.format(lst))
