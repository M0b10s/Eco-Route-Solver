import os


def print_Menu_Main():
    print("==========Bem Vindo ao Sistema da Eco-Route Solver==========")
    print("1 ==> Opções Frota")
    print("2 ==> Opções Encomendas")
    print("3 ==> Consultar Grafo")
    print("4 ==> Sair")


def print_Menu_Frota():
    print("==========Opções de Frota==========")
    print("1 ==> Adicionar á Frota")
    print("2 ==> Remover da Frota")
    print("3 ==> Consultar a Frota")
    print("4 ==> Sair de Opções de Frota")


def print_Menu_Encomenda():
    print("==========Opções de Serviços==========")
    print("1 ==> Adicionar a Encomendas")
    print("2 ==> Remover de Encomendas")
    print("3 ==> Consultar Encomendas")
    print("4 ==> Sair de Opções de Encomendas")


def invalid():
    print("Opção Inválida")
    input()


def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


def siga():
    print("Enter para continuar...")


def spacer():
    print("====================================================================================================")
    print("====================================================================================================")
    print()
