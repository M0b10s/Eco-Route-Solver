from Controler.Algoritmos import *
from Controler.Frota import *
from Controler.Grafo import cria_grafo, avaliar_estafeta
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
estafetas = []
melhor_alg = []

# Frota default (1 carro, 2 Motas, 3 Bikes)
sys_default_frota(frota, estafetas)
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

        match (input()):

            case "1":  # Menu Principal ==> Opções Frota

                while flag_frota:
                    clear()
                    print_Menu_Frota()

                    match (input()):

                        case "1":
                            adicionar_frota_ui(frota, estafetas)
                            organiza_frota(frota)
                        case "2":
                            remover_frota(frota)
                        case "3":
                            mostra_frota(frota)
                        case "4":
                            estafetas.sort(key=lambda estafeta: estafeta.rating, reverse=True)
                            mostra_estafetas(estafetas)
                        case "5":
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
                            servico.sort(key=lambda encomenda: encomenda.tempoEntrega)
                        case "2":
                            remover_Serv(servico, estafetas)
                        case "3":
                            mostra_servico(servico)
                            mostra_servico(servicoParaCarros)
                        case "4":
                            gera_n_rand(servico)
                            servico.sort(key=lambda encomenda: encomenda.tempoEntrega)
                        case "5":
                            flag_enc = False
                        case _:
                            invalid()

            case "3":
                consulta_grafo(grafo)

            case "4":  # MENU Principal ==> Algoritmos

                while flag_alg:

                    distribuirEncomendas(servicoParaCarros, servico, frota)
                    clear()
                    print_Menu_Op_Algoritmos()
                    flag_alg_inside = True

                    match (input()):

                        case "1":
                            clear()

                            while flag_alg_inside:
                                print_Menu_Algoritmos_Frota()
                                match (input()):

                                    case "1":
                                        print_Menu_Algoritmos_DFS()
                                        for f in frota:
                                            aVisitar = devolve_setores(f.get_listaEncomendas())
                                            print("\n")
                                            print("Setores a visitar: ")
                                            print(aVisitar)
                                            grafo.procura_DFS(aVisitar, f)
                                    case "2":
                                        print_Menu_Algoritmos_BFS()
                                        for f in frota:
                                            aVisitar = devolve_setores(f.get_listaEncomendas())
                                            print("\n")
                                            print("Setores a visitar: ")
                                            print(aVisitar)
                                            grafo.procura_BFS(aVisitar, f)

                                    case "3":
                                        print_Menu_Algoritmos_GREEDY()
                                        for f in frota:
                                            aVisitar = devolve_setores(f.get_listaEncomendas())
                                            print("\n")
                                            print("Setores a visitar: ")
                                            print(aVisitar)
                                            grafo.procura_greedy(aVisitar, f)

                                    case "4":
                                        print_Menu_Algoritmos_ASTAR()
                                        for f in frota:
                                            aVisitar = devolve_setores(f.get_listaEncomendas())
                                            print("\n")
                                            print("Setores a visitar: ")
                                            print(aVisitar)
                                            grafo.procura_aStar(aVisitar, f)

                                    case "5":
                                        for f in frota:
                                            print_Menu_Algoritmos_TODOS()
                                            aVisitar = devolve_setores(f.get_listaEncomendas())
                                            print("\n")
                                            print("Setores a visitar: ")
                                            print(aVisitar)

                                            print_Menu_Algoritmos_DFS()
                                            resultados = grafo.procura_DFS(aVisitar, f)
                                            custo = [resultado[1] for resultado in resultados]
                                            melhor_alg.append(sum(custo))

                                            print_Menu_Algoritmos_BFS()
                                            resultados = grafo.procura_BFS(aVisitar, f)
                                            custo = [resultado[1] for resultado in resultados]
                                            melhor_alg.append(sum(custo))

                                            print_Menu_Algoritmos_GREEDY()
                                            resultados = grafo.procura_greedy(aVisitar, f)
                                            custo = [resultado[1] for resultado in resultados]
                                            melhor_alg.append(sum(custo))

                                            print_Menu_Algoritmos_ASTAR()
                                            resultados = grafo.procura_aStar(aVisitar, f)
                                            custo = [resultado[1] for resultado in resultados]
                                            melhor_alg.append(sum(custo))

                                            if len(melhor_alg) > 0:
                                                print("\n")
                                                melhor = min(melhor_alg)

                                                melhor_algoritmo(melhor_alg.index(melhor))

                                                avaliar_estafeta(f, melhor)
                                                melhor_alg = []
                                                print("\n")
                                                spacer()

                                            f.get_listaEncomendas().clear()

                                    case "6":
                                        flag_alg_inside = False

                                    case _:
                                        invalid()

                        case "2":
                            clear()
                            veiculo_selecionado = None
                            while veiculo_selecionado is None:
                                mostra_frota_semEnc(frota)
                                id = int(input("Qual o id do veiculo a que deseja aplicar o algoritmo?\n"))
                                for veiculo in frota:
                                    if veiculo.get_last_id() == id:
                                        veiculo_selecionado = veiculo
                                        break

                                if veiculo_selecionado is None:
                                    print("O veiculo com o id selecionado não está disponivel!")

                            while flag_alg_inside:
                                print_Menu_Algoritmos_Veiculo()

                                match (input()):

                                    case "1":
                                        print_Menu_Algoritmos_DFS()
                                        aVisitar = devolve_setores(veiculo_selecionado.get_listaEncomendas())
                                        print("\n")
                                        print("Setores a visitar: ")
                                        print(aVisitar)
                                        resultados = grafo.procura_DFS(aVisitar, veiculo_selecionado)

                                    case "2":
                                        print_Menu_Algoritmos_BFS()
                                        aVisitar = devolve_setores(veiculo_selecionado.get_listaEncomendas())
                                        print("\n")
                                        print("Setores a visitar: ")
                                        print(aVisitar)
                                        resultados = grafo.procura_BFS(aVisitar, veiculo_selecionado)

                                    case "3":
                                        print_Menu_Algoritmos_GREEDY()
                                        aVisitar = devolve_setores(veiculo_selecionado.get_listaEncomendas())
                                        print("\n")
                                        print("Setores a visitar: ")
                                        print(aVisitar)
                                        resultados = grafo.procura_greedy(aVisitar, veiculo_selecionado)

                                    case "4":
                                        print_Menu_Algoritmos_ASTAR()
                                        aVisitar = devolve_setores(veiculo_selecionado.get_listaEncomendas())
                                        print("\n")
                                        print("Setores a visitar: ")
                                        print(aVisitar)
                                        resultados = grafo.procura_aStar(aVisitar, veiculo_selecionado)

                                    case "5":
                                        print_Menu_Algoritmos_TODOS()
                                        aVisitar = devolve_setores(veiculo_selecionado.get_listaEncomendas())
                                        print("\n")
                                        print("Setores a visitar: ")
                                        print(aVisitar)

                                        print_Menu_Algoritmos_DFS()
                                        resultados = grafo.procura_DFS(aVisitar, veiculo_selecionado)
                                        custo = [resultado[1] for resultado in resultados]
                                        melhor_alg.append(sum(custo))

                                        print_Menu_Algoritmos_BFS()
                                        resultados = grafo.procura_BFS(aVisitar, veiculo_selecionado)
                                        custo = [resultado[1] for resultado in resultados]
                                        melhor_alg.append(sum(custo))

                                        print_Menu_Algoritmos_GREEDY()
                                        resultados = grafo.procura_greedy(aVisitar, veiculo_selecionado)
                                        custo = [resultado[1] for resultado in resultados]
                                        melhor_alg.append(sum(custo))

                                        print_Menu_Algoritmos_ASTAR()
                                        resultados = grafo.procura_aStar(aVisitar, veiculo_selecionado)
                                        custo = [resultado[1] for resultado in resultados]
                                        melhor_alg.append(sum(custo))

                                    case "6":
                                        flag_alg_inside = False

                                if len(melhor_alg) > 0:
                                    print("\n")
                                    melhor = min(melhor_alg)
                                    melhor_algoritmo(melhor_alg.index(melhor))
                                    avaliar_estafeta(veiculo_selecionado, melhor)
                                    melhor_alg = []
                                    print("\n")
                                    spacer()
                                    veiculo_selecionado.get_listaEncomendas().clear()

                        case "3":
                            flag_alg = False

                        case _:
                            invalid()

            case "5":  # Menu Principal ==> Opção Sair

                flag = False

            case _:
                invalid()
