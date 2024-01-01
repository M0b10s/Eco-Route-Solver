from View.Menus import siga, spacer


def mostra_frota(frota):
    spacer()
    for v in frota:
        v.display()
        #for enc in v.get_listaEncomendas():
            #enc.display()
    print()
    siga()
    input()


def mostra_frota_semEnc(frota):
    spacer()
    for v in frota:
        v.display()
    print("\n")
    spacer()


def mostra_estafetas(estafetas):
    spacer()
    for e in estafetas:
        print(e)
        print("\n")
    print()
    siga()
    input()
