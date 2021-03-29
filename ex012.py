# Seno, cosseno, tangente
import math
num = float(input('Digite o ângulo desejado: '))
n1 = math.radians(num)                                         # float((num * math.pi)/180)
print()
print('{:^36}'.format('Para o ângulo {}°'.format(num)))
print('_' * 36)
print('|    SEN    |     COS   |   TAN    |')
print('-' * 36)
print('|   {:.3f}   |   {:.3f}   |  {:.3f}   |'.format(math.sin(n1), math.cos(n1), math.tan(n1)))
print('-' * 36)
