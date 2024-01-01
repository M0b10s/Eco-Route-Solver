class Estafeta:
    def __init__(self, id, idade, peso, rating, veiculo):
        self.id = id
        self.idade = idade
        self.peso = peso
        self.rating = rating
        self.veiculo = veiculo

    def fator_multiplicativo(self):
        fator_idade = 1 + self.idade * 0.1
        fator_peso = 1 + self.peso * 0.01

        fator_multiplicativo = fator_idade * fator_peso

        return fator_multiplicativo

    def set_veiculo(self, atrib):
        self.veiculo = atrib

    def get_veiculo(self):
        return self.veiculo

    def set_rating(self,rating):
        self.rating= rating

    def get_rating(self):
        return self.rating

    def __str__(self):
        return f"Estafeta {self.id} - Idade: {self.idade} anos, Peso: {self.peso} kg, Rating: {self.rating:.2f}, Veículo: {self.veiculo.get_classname()}"
