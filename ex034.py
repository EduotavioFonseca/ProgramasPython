from datetime import date
data = int(input('Digite o ano de nascimento: '))
print()
hoje = date.today().year
idade = hoje - data
if idade < 9:
    print('Sua idade é {} anos. ATLETA MIRIM.'.format(idade))
elif 9 <= idade < 14:
    print('Sua idade é {} anos. ATLETA INFANTIL.'.format(idade))
elif 14 <= idade < 19:
    print('Sua idade é {} anos. ATLETA JÚNIOR.'.format(idade))
elif 19 <= idade < 20:
    print('Sua idade é {} anos. ATLETA SÊNIOR.'.format(idade))
else:
    print('Sua idade é {} anos. ATLETA MASTER.'.format(idade))
