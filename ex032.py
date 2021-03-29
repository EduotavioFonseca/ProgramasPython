from datetime import date
data = int(input('Digite o ano de nascimento: '))
print()
hoje = date.today().year
idade = hoje - data
if  idade < 18:
    print('Ainda vai se alistar. Sua idade é {} anos. Faltam {} anos para se alistar.'.format(idade, 18 - idade))
elif  idade == 18:
    print('Está na hora de se alistar. Sua idade é {} anos.'.format(idade))
else:
    print('Já passou da hora de se alistar. Sua idade é {} anos. Passaram {} anos.'.format(idade, idade - 18))
