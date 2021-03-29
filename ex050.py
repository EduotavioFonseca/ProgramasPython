# Leitura com while
sexo = str(input('Digite o sexo [M/F]: ')).upper()
while sexo not in 'MF':
    print('Sexo inválido. Digite novamente.')
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
print('FIM')
