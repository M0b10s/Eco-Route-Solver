from Model.Encomenda import Encomenda
from Model.Veiculo import Veiculo


def separaEncomendas(servico, encomendasParaCarros):
    for s in servico:
        if s.get_volume() > 198000 or s.get_capacidade() > 20:  # VOLUME MAXIMO DE UMA MOTA/BICICLETA
            encomendasParaCarros.append(s)
            servico.remove(s)

def distribuirEncomendas(servicoParaCarros, servicos, frota):
    for f in frota:
        match(type(f)):

            case Carro:
                while f.get_pesoOcupado() < f.get_capacidade() and f.get_volumeOcupado < f.get_volume:
                    for sc in servicoParaCarros:
                        if f.get_pesoOcupado() + sc.peso < f.get_capacidade():
                            f.get_listaEncomendas.append(sc)
                            return servicoParaCarros.remove(sc)
                        else:
                            for s in servicos:
                                if f.get_pesoOcupado() + s.peso < f.get_capacidade():
