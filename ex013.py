# Sorteio de alunos
import random
al1 = input('Qual o nome do primeiro aluno? ')
print()
al2 = input('Qual o nome do segundo aluno? ')
print()
al3 = input('Qual o nome do terceiro aluno? ')
print()
al4 = input('Qual o nome do quarto aluno? ')
lst = [al1, al2, al3, al4]
escolhido = random.choice(lst)
print()
print('O aluno sorteado foi: {} .'.format(escolhido))
