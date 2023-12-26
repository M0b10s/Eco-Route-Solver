import os


def print_Menu_Main():
    print("==========Bem Vindo ao Sistema da Eco-Route Solver==========")
    print("1 ==> Opções Frota")
    print("2 ==> Opções Encomendas")
    print("3 ==> Consultar Grafo")
    print("4 ==> Iniciar Processamento")
    print("5 ==> Sair")


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
    print("4 ==> Gerar 'n' Encomendas Random")
    print("5 ==> Sair de Opções de Encomendas")


def print_Menu_Op_Algoritmos():
    print("==========Escolha a quem pretende aplicar o algoritmo==========")
    print("1 ==> Frota")
    print("2 ==> Veiculo")
    print("3 ==> Sair")

def print_Menu_Algoritmos_Frota():
    print("\n")
    print("==========Opções de Algoritmos(Frota)==========")
    print("1 ==> DFS")
    print("2 ==> BFS")
    print("3 ==> GREEDY")
    print("4 ==> A*")
    print("5 ==> TODOS")
    print("6 ==> Sair de Opções de Algoritmos")

def print_Menu_Algoritmos_Veiculo():
    print("\n")
    print("==========Opções de Algoritmos(Veiculo)==========")
    print("1 ==> DFS")
    print("2 ==> BFS")
    print("3 ==> GREEDY")
    print("4 ==> A*")
    print("5 ==> TODOS")
    print("6 ==> Sair de Opções de Algoritmos")

def print_Menu_Algoritmos_DFS():
    print("\n")
    print("==========ALGORTIMO DFS==========")

def print_Menu_Algoritmos_BFS():
    print("\n")
    print("==========ALGORTIMO BFS==========")

def print_Menu_Algoritmos_GREEDY():
    print("\n")
    print("==========ALGORTIMO GREEDY==========")

def print_Menu_Algoritmos_ASTAR():
    print("\n")
    print("==========ALGORTIMO A*==========")

def print_Menu_Algoritmos_TODOS():
    print("\n")
    print("==========TODOS OS ALGORITMOS==========")

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
