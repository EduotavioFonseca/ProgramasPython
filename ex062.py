# Lê idade e sexo usando while e break
soma = conth = contm = cont = contp18 = contm20 = 0
aux = 1
while True:
    print(f'------   {aux}ª Pessoa   ------')
    aux += 1
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    print('---------------------------')
    print()
    resp = str(input('Quer continuar? [S/N] ')).upper()
    print()
    cont += 1
    if idade > 18:
        contp18 += 1
    if sexo == 'M':
        conth += 1
    else:
        contm += 1
        if idade < 20:
            contm20 += 1
    if resp == 'N':
        break
print('= # =' * 10)
print()
print(f'Foram cadastradas {cont} pessoas.')
print()
print(f'Existem {contp18} pessoas com mais de 18 anos.')
print()
print(f'Foram cadastrados {conth} homens.')
print()
print(f'No grupo temos {contm20} mulheres com menos de 20 anos.')
print()
print('= # =' * 10)
