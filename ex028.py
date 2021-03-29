lado1 = float(input('Digite um lado do triângulo: '))
lado2 = float(input('Digite outro lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo: '))
print()
if abs(lado2 - lado3) < lado1 < lado2 + lado3:
    print('Os lados {}, {} e {} formam um triângulo.'.format(lado1, lado2, lado3))
else:
    print('Os lados {}, {} e {} não formam um triângulo.'.format(lado1, lado2, lado3))
