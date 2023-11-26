from Controler.Frota import *
from Controler.Servico import *

from View.Consulta_Servico import *
from View.Menus import *
from View.Consulta_frota import *

import os

# ==============================SYS INIT
# ==============================

frota = []
servico = []

# Frota default (1 carro, 2 Motas, 3 Bikes)
sys_default_frota(frota)

# ==============================
# ==============================SYS INIT END

if __name__ == '__main__':
    # vamos criar um for para percorrer a lista de frota

    # Menu de opções
    flag = True
    flag_frota = True
    flag_enc = True

    while flag:

        clear()
        flag_frota = True
        flag_enc = True
        print_Menu_Main()

        match (input()):

            case "1": # Menu Principal ==> Opções Frota

                while flag_frota:

                    clear()
                    print_Menu_Frota()

                    match(input()):

                        case "1":
                            adicionar_frota_ui(frota)
                        case "2":
                            remover_frota(frota)
                        case "3":
                            mostra_frota(frota)
                        case "4":
                            flag_frota = False
                        case _:
                            invalid()

            case "2": # Menu Principal ==> Opções Encomendas

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
                        case "4":
                            gera_n_rand(servico)
                        case "5":
                            flag_enc = False
                        case _:
                            invalid()

            case "3": # Menu Principal ==> Opção Sair

                flag = False

            case _:
                invalid()
