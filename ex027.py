salario = float(input('Qual o seu salário? R$ '))
print()
if salario > 1250:
    print('O seu aumento será de: R$ {:.2f}.'.format(salario * 1.1))
else:
    print('O seu aumento será de: R$ {:.2f}.'.format(salario * 1.15))
