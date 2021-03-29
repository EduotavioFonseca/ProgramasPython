# Função fatorial com 2 parâmetros
def fatorial(num, show = False):
    fat = 1
    if num == 0:
        return 1
    if num > 0:
        while num > 0:
            fat *= num
            if show:
                if num > 1:
                    print(f'{num} x', end=' ')
                else:
                    print(f'{num} =', end=' ')
            num -= 1
        return f'{fat}'
    else:
       return "Não existe fatorial de número negativo."


print()
print('-' * 50)
print(fatorial(8, True))
