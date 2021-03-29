# Menu para o exercício ex097

def criaArquivo():
    arq1 = open('arquivo1.txt', 'w+')
    arq1.close()
    print('arquivo1.txt criado com êxito.')
    print()


def mensagem():
    print('-' * 40)
    print('Menu Principal'.center(40))
    print('-' * 40)
    print('\t 1- Ver pessoas cadastradas')
    print('\t 2- Cadastrar novas pessoas')
    print('\t 3- Sair do Sistema')
    print('-' * 40)
    opc = str(input('Digite a sua opção: '))
    if opc == '1':
        a = open('arquivo1.txt', 'r')
        print(a.read())
        a.close()
    elif opc == '2':
        novocadastro()
    elif opc == '3':
        saidasist()
    else:
        print()
        print('Opção Inválida!!! Digite 1, 2 ou 3.')
        print()
        mensagem()


def novocadastro():
    print('-' * 40)
    print('Novo Cadastro'.center(40))
    print('-' * 40)
    nome = str(input('Digite o nome: '))
    print()
    idade = int(input('Digite a idade: '))
    print('-' * 40)


def saidasist():
    print('-' * 40)
    print('\t Saindo do Sistema ... Até logo!!! ')
    print('-' * 40)
    print()


def cadastrar():


mensagem()


