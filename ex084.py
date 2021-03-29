# Cadastros num dicionário
from _datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input('Digite o nome: '))
ano = int(input('Digite o ano de nascimento: '))
cadastro['Idade'] = (datetime.now().year - ano)
cadastro['CTPS'] = int(input('Digite o número da CTPS (0 não tem): '))
if cadastro['CTPS'] != 0:
    cadastro['Contratacao'] = int(input('Digite o ano de contratação: '))
    cadastro['Salario'] = float(input('Digite o salário: R$ '))
    cadastro['Aposentadoria'] = 35 - ano + cadastro['Contratacao']
else:
    cadastro['CTPS'] = 0
print()
for k, v in cadastro.items():
    print(f'{k} tem o valor: {v}')
