from Controler.Algoritmos import *
from Controler.Frota import *
from Controler.Grafo import cria_grafo
from Controler.Servico import *
from Controler.DistribuirEncomendas import *
from Controler.Grafo import Grafo
from View.Consulta_grafo import *
from View.Consulta_Servico import *
from View.Menus import *
from View.Consulta_frota import *
from View import *

import os

# ==============================SYS INIT
# ==============================

frota = []
servico = []
servicoParaCarros = []
grafo = cria_grafo()

# Frota default (1 carro, 2 Motas, 3 Bikes)
sys_default_frota(frota)
organiza_frota(frota)

# ==============================
# ==============================SYS INIT END

if __name__ == '__main__':
    # vamos criar um for para percorrer a lista de frota

    # Menu de opções
    flag = True
    flag_frota = True
    flag_enc = True
    flag_alg = True
    flag_alg_inside = True

    while flag:

        clear()
        flag_frota = True
        flag_enc = True
        flag_alg = True
        print_Menu_Main()

        match(input()):

            case "1":  # Menu Principal ==> Opções Frota

                while flag_frota:

                    clear()
                    print_Menu_Frota()

                    match (input()):

                        case "1":
                            adicionar_frota_ui(frota)
                            organiza_frota(frota)
                        case "2":
                            remover_frota(frota)
                        case "3":
                            mostra_frota(frota)
                        case "4":
                            flag_frota = False
                        case _:
                            invalid()

            case "2":  # Menu Principal ==> Opções Encomendas

                while flag_enc:

                    clear()
                    print_Menu_Encomenda()

                    match (input()):

                        case "1":
                            criar_Serv(servico)
                        case "2":
                            remover_Serv(servico)
                        case "3":
                            mostra_servico(servico)
                            mostra_servico(servicoParaCarros)
                        case "4":
                            gera_n_rand(servico)
                        case "5":
                            flag_enc = False
                        case _:
                            invalid()

            case "3":
                consulta_grafo(grafo)

            case "4": # MENU Principal ==> Algoritmos

                while flag_alg:

                    distribuirEncomendas(servicoParaCarros, servico, frota)
                    clear()
                    print_Menu_Op_Algoritmos()
                    flag_alg_inside = True

                    match (input()):

                        case "1":
                            clear()
                            print_Menu_Algoritmos_Frota()

                            while flag_alg_inside:
                                match (input()):

                                    case "1":
                                        for f in frota:
                                            aVisitar = devolve_setores(f.get_listaEncomendas())
                                            grafo.procura_DFS(aVisitar)
                                    case "2":
                                        for f in frota:
                                            aVisitar = devolve_setores(f.get_listaEncomendas())
                                            grafo.procura_BFS(aVisitar)

                                    case "3":
                                        for f in frota:
                                            greedy_search(f,grafo)

                                    case "4":
                                        "A*"

                                    case "5":
                                        "todos"

                                    case "6":
                                        flag_alg_inside = False

                                    case _:
                                        invalid()

                        case "2":
                            clear()
                            # ADICIONAR PRINT DE TODOS OS VEICULOS EM FALTA
                            print_Menu_Algoritmos_Veiculo()

                            while flag_alg_inside:
                                match (input()):

                                    case "1":
                                        "dfs"

                                    case "2":
                                        "bfs"

                                    case "3":
                                        "greedy"

                                    case "4":
                                        "A*"

                                    case "5":
                                        "todos"

                                    case "6":
                                        flag_alg_inside = False

                        case "3":
                            flag_alg = False

                        case _:
                            invalid()

            case "5":  # Menu Principal ==> Opção Sair

                flag = False

            case _:
                invalid()
