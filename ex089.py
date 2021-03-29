# Função com mensagem adaptável
def escreva(txt):
    txt.strip()
    contador = len(txt)
    print('-' * contador)
    print(txt)
    print('-' * contador)


lista = str(input('Digite uma frase qualquer: ')).upper()
print()
escreva(lista)
