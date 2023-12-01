class Veiculo:
    last_id = 1

    def __init__(self, capacidade, velMedia, penalizacaoPorPeso, volume, volumeOcupado, pesoOcupado):
        self.capacidade = capacidade
        self.velMedia = velMedia
        self.penalizacaoPorPeso = penalizacaoPorPeso
        self.last_id = Veiculo.last_id
        self.listaEncomendas = []
        self.volume = volume
        self.volumeOcupado = volumeOcupado
        self.pesoOcupado = pesoOcupado

    def display(self):
        print(f"ID: {self.last_id}, "
              f"Tipo: {self.__class__.__name__}, "
              f"Capacidade: {self.capacidade}, "
              f"Volume: {self.volume} cm³, "
              f"Velocidade média: {self.velMedia}, "
              f"Penalização por peso: {self.penalizacaoPorPeso}, "
              f"Lista de Encomendas: {self.listaEncomendas}, "
              f"Volume Ocupado: {self.volumeOcupado} cm³, "
              f"Peso Ocupado: {self.pesoOcupado} kg, ")

    def get_capacidade(self):
        return self.capacidade

    def get_velMedia(self):
        return self.velMedia

    def get_penalizacaoPorPeso(self):
        return self.penalizacaoPorPeso

    def get_last_id(self):
        return self.last_id

    def get_listaEncomendas(self):
        return self.listaEncomendas

    def get_volume(self):
        return self.volume

    def get_volumeOcupado(self):
        return self.volumeOcupado

    def get_pesoOcupado(self):
        return self.pesoOcupado

    def set_capacidade(self, capacidade):
        self.capacidade = capacidade

    def set_velMedia(self, velMedia):
        self.velMedia = velMedia

    def set_penalizacaoPorPeso(self, penalizacaoPorPeso):
        self.penalizacaoPorPeso = penalizacaoPorPeso

    def set_listaEncomendas(self, listaEncomendas):
        self.listaEncomendas = listaEncomendas

    def set_volume(self, volume):
        self.volume = volume

    def set_volumeOcupado(self, volumeOcupado):
        self.volumeOcupado = volumeOcupado

    def set_pesoOcupado(self, pesoOcupado):
        self.pesoOcupado = pesoOcupado

# subclass
class Carro(Veiculo):
    def __init__(self, capacidade=100, velMedia=50, penalizacaoPorPeso=0.1, volume=160 * 140 * 110,volumeOcupado = 0, pesoOcupado = 0):
        super().__init__(capacidade, velMedia, penalizacaoPorPeso, volume, volumeOcupado,pesoOcupado)
        self.capacidade = capacidade
        self.velMedia = velMedia
        self.penalizacaoPorPeso = penalizacaoPorPeso
        self.last_id = Carro.last_id
        Veiculo.last_id += 1


class Mota(Veiculo):
    def __init__(self, capacidade=20, velMedia=35, penalizacaoPorPeso=0.5, volume=55 * 60 * 60 * 3, volumeOcupado = 0, pesoOcupado = 0):
        super().__init__(capacidade, velMedia, penalizacaoPorPeso, volume, volumeOcupado, pesoOcupado)
        self.capacidade = capacidade
        self.velMedia = velMedia
        self.penalizacaoPorPeso = penalizacaoPorPeso
        self.last_id = Carro.last_id
        Veiculo.last_id += 1


class Bicicleta(Veiculo):
    def __init__(self, capacidade=5, velMedia=10, penalizacaoPorPeso=0.6, volume=55 * 60 * 60, volumeOcupado = 0, pesoOcupado = 0):
        super().__init__(capacidade, velMedia, penalizacaoPorPeso, volume, volumeOcupado, pesoOcupado)
        self.capacidade = capacidade
        self.velMedia = velMedia
        self.penalizacaoPorPeso = penalizacaoPorPeso
        self.last_id = Carro.last_id
        Veiculo.last_id += 1
