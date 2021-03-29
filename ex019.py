#Pegando início de nome
cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()
aux1 = cidade.split()
print()
print('Essa cidade começa com a palavra Santo?')
print('SANTO' in aux1[0])
