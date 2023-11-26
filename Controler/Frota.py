from Model.Veiculo import Carro, Mota, Bicicleta
from View.Menus import *


def criar_frota(tipo, qtd, frota):
    if tipo == "Carro":
        for i in range(qtd):
            v = Carro()
            frota.append(v)

    elif tipo == "Mota":
        for i in range(qtd):
            v = Mota()
            frota.append(v)

    elif tipo == "Bicicleta":
        for i in range(qtd):
            v = Bicicleta()
            frota.append(v)


def adicionar_frota_ui(frota):
    spacer()
    tipo = ""
    quantidade = 0

    while tipo != "Carro" and tipo != "Mota" and tipo != "Bicicleta":
        print("Que Tipo de Veiculo quer adicionar?")
        tipo = input()
        tipo = tipo.lower()
        tipo = tipo.capitalize()

    try:
        print("Quantos Veiculos deste tipo deseja adicionar?")
        quantidade = int(input())
    except ValueError:
        print("Input inválido. Adição de Veiculo cancelada, Voltando ao menu principal")
        siga()
        input()

    criar_frota(tipo, quantidade, frota)
    print("Sucesso!")
    print(f"Foram criadas {quantidade} {tipo}"f"s")
    siga()
    input()


def remover_frota(frota):
    for v in frota:
        v.display()
    print("Qual o Id a remover?")
    id_rem = int(input())
    i = 1
    for v in frota:
        i += 1
        if v.get_id() == id_rem:
            frota = frota.pop(i)


def sys_default(frota):
    criar_frota("Carro", 1, frota)
    criar_frota("Mota", 2, frota)
    criar_frota("Bicicleta", 3, frota)
