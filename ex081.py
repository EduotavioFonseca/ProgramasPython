# Média de notas de alunos
import statistics
lista1 = []
lista2 = []
while True:
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    lista1.append(aluno)
    lista2.append(nota1)
    lista2.append(nota2)
    lista1.append(lista2[:])
    lista2.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    print()
    if resp == 'N':
        break
print()
print(f'A lista de notas é: {lista1}')
print()
print('      Média do aluno')
print('-' * 32)
for a in range(0, len(lista1), 2):
    print(f'{lista1[a]:15}   {statistics.mean(lista1[a+1])} ')
    print('-' * 26)
print()
print(f'           Notas individuais')
print('-' * 40)
consulta = ' '
while consulta not in '999':
    consulta = str(input('Digite o nome do aluno: '))
    for i in range(0, len(lista1), 2):
        if consulta == lista1[i]:
            print(f'As notas do aluno {lista1[i]} são: {lista1[i + 1]}')
        elif consulta != lista1[i]:
            pass
    print()
    if consulta == '999':
        break
