from Model.Encomenda import *
from View.Menus import spacer, siga

import random
import math


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

    try:
        comprimento = 0
        while comprimento < 1 or comprimento > 160:
            print("Qual o comprimento da sua Encomenda?(1<=comprimento<=160)")
            comprimento = int(input())
    except ValueError:
        print("Input inválido. Adição de Encomenda cancelada, Voltando ao menu principal")
        siga()
        input()

    try:
        largura = 0
        while largura < 1 or largura > 140:
            print("Qual a largura da sua Encomenda?(1<=largura<=140)")
            largura = int(input())
    except ValueError:
        print("Input inválido. Adição de Encomenda cancelada, Voltando ao menu principal")
        siga()
        input()

    try:
        altura = 0
        while altura < 1 or altura > 110:
            print("Qual a altura da sua Encomenda?(1<=altura<=110)")
            altura = int(input())
    except ValueError:
        print("Input inválido. Adição de Encomenda cancelada, Voltando ao menu principal")
        siga()
        input()

    try:
        tempoEntrega = 0
        while tempoEntrega < 1 or tempoEntrega > 24:
            print("Qual é o tempo de entrega da sua Encomenda?(1<=tempoEntrega<=24)")
            tempoEntrega = int(input())
    except ValueError:
        print("Input inválido. Adição de Encomenda cancelada, Voltando ao menu principal")
        siga()
        input()

    e = Encomenda(peso, dest, comprimento, largura, altura, tempoEntrega * 60)

    servico.append(e)
    organiza_servico(servico)


def remover_Serv(servicos,estafetas):
    for v in servicos:
        v.display()
    print("Qual o Id a remover?")
    id_rem = int(input())
    i = 0
    for v in servicos:
        if v.get_id() == id_rem:
            servicos = servicos.pop(i)
            remover_Estafeta(estafetas, id_rem)
        i += 1

def remover_Estafeta(estafetas,id_rem):
    for e in estafetas:
        print(e.get_veiculo().get_last_id())
        print(id_rem)
        if e.get_veiculo().get_last_id() == id_rem:
            estafetas.pop(e)
        input()


def gera_n_rand(servico):
    try:
        n = 0
        print("Quantas Encomendas deseja gerar?")
        n = int(input())
    except ValueError:
        print("Input inválido. Adição de Encomenda cancelada, Voltando ao menu principal")
        siga()
        input()

    for i in range(n):
        # Gera peso com distribuição exponencial negativa
        peso = round(-math.log(random.random()) * 10) + 1
        dest = random.randint(1, 12)
        altura = random.randint(1, 110)
        comprimento = random.randint(1, 160)
        largura = random.randint(1, 140)
        tempoEntrega = random.randint(1, 100)

        e = Encomenda(peso, dest, comprimento, largura, altura, tempoEntrega)
        servico.append(e)


def organiza_servico(servico):
    servico_organizado = sorted(servico, key=lambda encomenda: encomenda.tempoEntrega)
    return servico_organizado
