preco = float(input('Qual é o valor da casa? '))
salario = float(input('Qual o seu salário atual? '))
ano = int(input('Em quantos anos quer pagar a casa? '))
prestacao = float(preco/(ano*12))
print()
if prestacao <= salario * 0.3:
    print('Você pode pagar R$ {:.2f} de prestação em {} anos.'.format(prestacao, ano))
else:
    print('Empréstimo negado. A prestação de R$ {} deve ser inferior a 30% do seu salário.'.format(prestacao))
