peso = float(input('Digite o peso em kg: '))
alt = float(input('Digite a altura em m: '))
imc = peso/pow(alt, 2)
print()
if imc < 18.5:
    print('Seu imc é {:.2f}. Você está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu imc é {:.2f}. Você está com peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu imc é {:.2f}. Você está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu imc é {:.2f}. Você está com obesidade'.format(imc))
else:
    print('Seu imc é {:.2f}. Você está com obesidade mórbida'.format(imc))
