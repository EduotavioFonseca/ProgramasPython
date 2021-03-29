# Nome, idade e sexo
soma = maior = count = 0
aux = ''
for i in range(1, 5):
    print('----- {}ª Pessoa -----'.format(i))
    nome = str(input('Digite o nome: ')).upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    soma += idade
    if sexo == 'M':
        if i == 1:
            maior = idade
            aux = nome
        else:
            if idade > maior:
                maior = idade
                aux = nome
    else:
        if idade < 20:
            count += 1
print()
print('A média de idade do grupo é {:.2f} anos.'.format(soma/4))
print('O homem mais velho é {} e ele tem {} anos.'.format(aux, maior))
print('No grupo temos {} mulheres com menos de 20 anos.'.format(count))
