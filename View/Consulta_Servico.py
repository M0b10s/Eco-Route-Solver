from View.Menus import siga, spacer
def mostra_servico(servicos):
    spacer()
    for v in servicos:
        v.display()
    print()
    siga()
    input()