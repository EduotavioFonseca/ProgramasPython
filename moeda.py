# Módulo com funções

def aumentar(preco, taxa):
    aumento = (1 + taxa/100) * preco
    return aumento

def diminuir(preco, taxa):
    diminui = (1 - taxa/100) * preco
    return diminui

def dobro(preco):
    dobrar = 2 * preco
    return dobrar

def metade(preco):
    meio = 0.5 * preco
    return meio

