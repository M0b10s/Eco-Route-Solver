class Encomenda:
    last_id = 1

    def __init__(self, peso, destino, comprimento, largura, altura, tempoEntrega):
        self.id = Encomenda.last_id
        self.peso = peso
        self.destino = destino
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura
        self.tempoEntrega = tempoEntrega
        self.volume = comprimento * largura * altura
        Encomenda.last_id += 1

    def display(self):
        print(f"ID: {self.id}, "
              f"Peso: {self.peso} kg, "
              f"Destino: {self.destino}, "
              f"Dimensões: {self.comprimento} x {self.largura} x {self.altura} cm, "
              f"Volume: {self.volume} cm³, "
              f"Tempo de Entrega: {self.tempoEntrega} minutos")

    def get_id(self):
        return self.id

    def get_peso(self):
        return self.peso

    def get_destino(self):
        return self.destino

    def get_comprimento(self):
        return self.comprimento

    def get_largura(self):
        return self.largura

    def get_altura(self):
        return self.altura

    def get_tempoEntrega(self):
        return self.tempoEntrega

    def get_volume(self):
        return self.volume


