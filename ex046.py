# Palíndromos
frase = str(input('Digite uma frase: ')).strip()
a = frase.split()
junta = ''.join(a)
b = junta[::-1]
if b == junta:
    print('A frase {} é um PALÍNDROMO.'.format(frase))
else:
    print('A frase {} não é um PALÍNDROMO.'.format(frase))
