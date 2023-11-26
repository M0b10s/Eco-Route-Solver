from Model.Encomenda import *
from View.Menus import spacer, siga


def criar_Serv(servico):
    global dest
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
        return False

    try:
        dest = 0
        while dest < 1 or dest > 12:
            print("Qual o destino da sua Encomenda?(0<destino<13)")
            dest = int(input())
    except ValueError:
        print("Input inválido. Adição de Encomenda cancelada, Voltando ao menu principal")
        siga()
        input()

    e = Encomenda(peso, dest)

    servico.append(e)


def remover_Serv(servicos):
    for v in servicos:
        v.display()
    print("Qual o Id a remover?")
    id_rem = int(input())
    i = 0
    for v in servicos:
        if v.get_id() == id_rem:
            servicos = servicos.pop(i)
        i += 1
