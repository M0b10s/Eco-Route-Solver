from Model.Encomenda import Encomenda
from Model.Veiculo import Veiculo, Carro, Bicicleta, Mota


def separaEncomendas(servico, encomendasParaCarros):
    for s in servico:
        if s.get_volume() > 198000 or s.get_peso() > 20:  # VOLUME MAXIMO DE UMA MOTA/BICICLETA
            encomendasParaCarros.append(s)
            servico.remove(s)


def distribuirEncomendas(servicoParaCarros, servicos, frota):
    separaEncomendas(servicos, servicoParaCarros)
    for f in frota:
        match f:
            case Carro():
                    for sc in servicoParaCarros:
                        if f.get_pesoOcupado() + sc.get_peso() < f.get_capacidade() and f.get_volumeOcupado() + sc.get_volume() < f.get_volume():
                            f.get_listaEncomendas().append(sc)
                            f.set_pesoOcupado(sc.get_peso() + f.get_pesoOcupado())
                            f.set_volumeOcupado(sc.get_volume() + f.get_volumeOcupado())
                            servicoParaCarros.remove(sc)
                        else:
                            continue

                    for s in servicos:
                        if f.get_pesoOcupado() + s.get_peso() < f.get_capacidade() and f.get_volumeOcupado() + s.get_volume() < f.get_volume():
                            f.get_listaEncomendas().append(s)
                            f.set_pesoOcupado(s.get_peso() + f.get_pesoOcupado())
                            f.set_volumeOcupado(s.get_volume() + f.get_volumeOcupado())
                            servicos.remove(s)
                        else:
                            continue

            case _:
                    for s in servicos:
                        if f.get_pesoOcupado() + s.get_peso() < f.get_capacidade() and f.get_volumeOcupado() + s.get_volume() < f.get_volume():
                            f.get_listaEncomendas().append(s)
                            f.set_pesoOcupado(s.get_peso() + f.get_pesoOcupado())
                            f.set_volumeOcupado(s.get_volume() + f.get_volumeOcupado())
                            servicos.remove(s)
                        else:
                            continue
