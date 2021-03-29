# Área da parede
n1 = float(input('Qual a altura da parede em m? '))
n2 = float(input('Qual a largura da parede em m? '))
print()
print('A área da parede é: {} m². Considerando que 1l de tinta pinta 2 m², você vai gastar {:.2f}l de tinta.'.format(n1*n2, n1*n2/2))
