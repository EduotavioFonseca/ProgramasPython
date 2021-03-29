import statistics
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
notas = [n1, n2]
med = statistics.mean(notas)
print()
if med < 5:
    print('Sua média é {:.2f}. Você foi reprovado!!! Média inferior a 5.0'.format(med))
elif 5 <= med < 6.9:
    print('Sua média é {:.2f}. Você está de recuperação. Média entre 5.0 e 6.9'.format(med))
else:
    print('Sua média é {:.2f}. Parabéns!!! Você foi aprovado. Média superior a 6.9'.format(med))
