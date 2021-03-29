# Função que recebe o ano e retorna voto
def voto(ano):
    from datetime import datetime
    data = datetime.now().year - ano
    if data < 16:
        return print(f'Com {data} anos: VOTO NEGADO.')
    elif 16 <= data < 18 or data >= 65:
        return print(f'Com {data} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {data} anos: VOTO OBRIGATÓRIO.')


nasc = int(input('Em que ano você nasceu? '))
print('---------------------------------')
voto(nasc)
