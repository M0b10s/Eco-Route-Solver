class Veiculo:
    last_id = 1

    def __init__(self, capacidade, velMedia, penalizacaoPorPeso):
        self.capacidade = capacidade
        self.velMedia = velMedia
        self.penalizacaoPorPeso = penalizacaoPorPeso
        self.last_id = Veiculo.last_id

    def display(self):
        print(f"ID: {self.last_id}, "
              f"Tipo: {self.__class__.__name__}, "
              f"Capacidade: {self.capacidade}, "
              f"Velocidade média: {self.velMedia}, "
              f"Penalização por peso: {self.penalizacaoPorPeso}")

    def get_id(self):
        return self.last_id


# subclass
class Carro(Veiculo):
    def __init__(self, capacidade=50, velMedia=100, penalizacaoPorPeso=0.1):
        super().__init__(capacidade, velMedia, penalizacaoPorPeso)
        self.capacidade = capacidade
        self.velMedia = velMedia
        self.penalizacaoPorPeso = penalizacaoPorPeso
        self.last_id = Carro.last_id
        Veiculo.last_id += 1


class Mota(Veiculo):
    def __init__(self, capacidade=20, velMedia=35, penalizacaoPorPeso=0.5):
        super().__init__(capacidade, velMedia, penalizacaoPorPeso)
        self.capacidade = capacidade
        self.velMedia = velMedia
        self.penalizacaoPorPeso = penalizacaoPorPeso
        self.last_id = Carro.last_id
        Veiculo.last_id += 1


class Bicicleta(Veiculo):
    def __init__(self, capacidade=5, velMedia=10, penalizacaoPorPeso=0.6):
        super().__init__(capacidade, velMedia, penalizacaoPorPeso)
        self.capacidade = capacidade
        self.velMedia = velMedia
        self.penalizacaoPorPeso = penalizacaoPorPeso
        self.last_id = Carro.last_id
        Veiculo.last_id += 1
