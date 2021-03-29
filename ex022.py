# Excesso de velocidade
vel = float(input('Qual a sua velocidade em km/h? '))
print()
if vel > 80:
    print('Pare!!! Você foi multado em R$ {:.2f} por exceder a velocidade de 80 km/h.'.format((vel - 80)*7))
else:
    print('Parabéns!!!. Sua velocidade está no limite de 80 km/h.')
