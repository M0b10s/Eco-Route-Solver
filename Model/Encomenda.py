class Encomenda:
    last_id = 1

    def __init__(self, id, peso, destino):
        self.id = id
        self.peso = peso
        self.destino = destino
        self.id = self.last_id
        Encomenda.last_id += 1

    def display(self):
        print(f"ID: {self.id}, "
              f"Peso: {self.peso}, "
              f"Destino: {self.destino}")

    def get_id(self):
        return self.last_id

