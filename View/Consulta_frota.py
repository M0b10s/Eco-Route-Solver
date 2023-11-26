from View.Menus import siga, spacer


def mostra_frota(frota):
    spacer()
    for v in frota:
        v.display()
    print()
    siga()
    input()
