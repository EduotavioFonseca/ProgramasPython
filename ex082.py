# Dicionário com nome e média do aluno. Dá a situação final (>= 7 Aprovado, < 7 Reprovado)
cadastro = {}
cadastro['aluno'] = str(input('Digite o nome do aluno: '))
cadastro['media'] = float(input('Digite a média do aluno: '))
if cadastro['media'] >= 7:
    cadastro['situacao'] = 'APROVADO'
else:
    cadastro['situacao'] = 'REPROVADO'
print()
print(f'O nome do aluno é: {cadastro["aluno"]}')
print()
print(f'Sua média é: {cadastro["media"]}')
print()
print(f'Ele está: {cadastro["situacao"]}')
