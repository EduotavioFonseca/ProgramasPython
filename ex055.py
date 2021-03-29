# Sequência Fibonacci: Fn = F(n-1) + F(n-2)
termos = int(input('Quantos termos da sequência de Fibonacci deseja calcular? '))
print()
fibo = f1 = troca = 0
i = 0
f2 = 1
print('Os {} primeiros termos da sequência são: '.format(termos, end=' '))
while i < termos:
    print(fibo, end=' ')
    troca = fibo
    f1 = f2
    f2 = troca
    fibo = f1 + f2
    i += 1
