import random, time
print('{:=^75}'.format(' JOKENPO '))
print()
print('{:=^75}'.format('Escolha uma das opções abaixo'))
print()
print('{:^75}'.format('1 - PEDRA'))
print('{:^75}'.format('2 - PAPEL'))
print('{:^75}'.format('3 - TESOURA'))
print()
print('=^=' * 25)
lst = ['pedra', 'papel', 'tesoura']
computador = random.randint(1, 3)
escolha = int(input('{:^75}'.format('JOGAR!!!  ')))
print()
print('{:^75}'.format('JO'))
time.sleep(2)
print('{:^75}'.format('KEN'))
time.sleep(2)
print('{:^75}'.format('PO!'))
print()
print('=^=' * 25)
if computador == 1:
    if escolha == 1:
        print('O computador escolheu {} e você escolheu {}. EMPATE. Jogue de novo'.format(lst[0], lst[0]))
        if escolha == 2:
            print('O computador escolheu {} e você escolheu {}. Você GANHOU!!!'.format(lst[0], lst[1]))
    else:
        print('O computador escolheu {} e você escolheu {}. Você PERDEU!!!'.format(lst[0], lst[2]))

elif computador == 2:
    if escolha == 1:
        print('O computador escolheu {} e você escolheu {}. Você PERDEU!!!'.format(lst[1], lst[0]))
        if escolha == 2:
            print('O computador escolheu {} e você escolheu {}. EMPATE. Jogue de novo.'.format(lst[1], lst[1]))
    else:
        print('O computador escolheu {} e você escolheu {}. Você GANHOU!!!'.format(lst[1], lst[2]))

if computador == 3:
    if escolha == 1:
        print('O computador escolheu {} e você escolheu {}. Você GANHOU!!!'.format(lst[2], lst[0]))
        if escolha == 2:
            print('O computador escolheu {} e você escolheu {}. Você PERDEU!!!'.format(lst[2], lst[1]))
    else:
        print('O computador escolheu {} e você escolheu {}. EMPATE. Jogue de novo.'.format(lst[2], lst[2]))
print('=^=' * 25)
