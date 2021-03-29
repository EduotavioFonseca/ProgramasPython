# Função notas com dicionário
from statistics import mean
def notas(*num, sit=False):
    print(num)
    m = mean(num)
    geral = {'total':len(num), 'maior':max(num), 'menor':min(num), 'média':m}
    if sit == True:
        if 0 < m < 5:
            geral['situação'] = 'RUIM'
        if 5 <= m < 7:
            geral['situação'] = 'MÉDIA'
        if m >= 7:
            geral['situação'] = 'BOA'
    return geral


resp = notas(2, 3, 4, sit=False)
print(resp)
resp = notas(2, 3, 4, 6, 7, 9, sit=True)
print(resp)
