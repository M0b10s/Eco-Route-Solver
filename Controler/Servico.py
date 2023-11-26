from Model.Encomenda import *
from View.Menus import spacer,siga


def criar_Serv(servico):
    spacer()
    try:
        peso = 0
        while peso <= 0 or peso > 100:
            print("Qual o peso da sua Encomenda?(0<peso<100)")
            peso = int(input())
    except ValueError:
        print("Input inválido. Adição de Encomenda cancelada, Voltando ao menu principal")
        siga()
        input()

    try:
        dest = 0
        while dest < 1 or dest > 12:
            print("Qual o destino da sua Encomenda?(0<destino<13)")
            peso = int(input())
    except ValueError:
        print("Input inválido. Adição de Encomenda cancelada, Voltando ao menu principal")
        siga()
        input()

    s
