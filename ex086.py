# Dicionário de pessoas dentro de uma lista.
colecao = {}
tabela = []
soma = 0
while True:
    colecao['Nome'] = str(input('Digite o nome da pessoa: '))
    print()
    while True:
        colecao['Sexo'] = str(input('Digite o sexo [M/F]: ')).upper()
        if colecao['Sexo'] in 'MF':
            break
        print('ERRO!!! Digite apenas M ou F.')
    print()
    colecao['Idade'] = int(input('Digite a idade da pessoa: '))
    soma += colecao['Idade']
    print()
    tabela.append(colecao.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO!!! Digite apenas S ou N.')
    print()
    if resp == 'N':
        break
print(tabela)
print()
print(f'O grupo tem {len(tabela)} pessoas.')
print()
print(f'A média de idade das pessoas é: {(soma/len(tabela)):.2f} anos.')
print()
print(f'As mulheres do grupo são: ', end=' ')
for p in tabela:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print()
print(f'Lista das pessoas com idade acima da média: ', end=' ')
for p in tabela:
    if p['Idade'] >= (soma/len(tabela)):
        for k, v in p.items():
            print(f'{k} : {v}', end=' ', )
    print()
print()
